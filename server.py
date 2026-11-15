import json
import os
import shutil
import tempfile
import traceback
import zipfile
from collections import Counter
from typing import List

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# ---- Adjust to your file names if different ----
from main import CodeReviewer     # file that contains class CodeReviewer
from vector_store import VectorStore
# -------------------------------------------------

app = FastAPI(title="CodeLens")

reviewer = CodeReviewer()
state = {"project": None, "root": None, "tmp": None, "history": []}


class ChatIn(BaseModel):
    message: str


class ProjectIn(BaseModel):
    path: str


def rel(path):
    try:
        return os.path.relpath(path, state["root"])
    except ValueError:
        return path


def load(root, name):
    if not os.path.isdir(root):
        raise HTTPException(400, f"Folder not found: {root}")

    # fresh index so projects never get mixed together
    reviewer.vector_store = VectorStore()
    reviewer.agent.memory.clear()
    try:
        reviewer.load_project(root)
    except Exception as e:
        raise HTTPException(
            500, f"Could not load this project (does it contain supported source files?): {e}"
        )

    metas = reviewer.vector_store.metadatas
    if not metas:
        raise HTTPException(400, "No supported source files found (.py, .js, .ts, .java, .cpp, .go ...).")

    files = {m["path"]: m["language"] for m in metas}
    state.update(
        root=root,
        history=[],
        project={
            "name": name,
            "path": root,
            "files": len(files),
            "chunks": len(metas),
            "languages": dict(Counter(files.values()).most_common()),
        },
    )
    return state["project"]


@app.get("/api/state")
def get_state():
    return {"project": state["project"], "history": state["history"]}


@app.post("/api/project")
def load_path(body: ProjectIn):
    root = os.path.abspath(os.path.expanduser(body.path.strip()))
    return {"project": load(root, os.path.basename(root) or root)}


@app.post("/api/project/zip")
def load_zip(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".zip"):
        raise HTTPException(400, "Please upload a .zip file.")
    if state["tmp"]:
        shutil.rmtree(state["tmp"], ignore_errors=True)
    tmp = tempfile.mkdtemp(prefix="codelens_")
    state["tmp"] = tmp
    zpath = os.path.join(tmp, "upload.zip")
    with open(zpath, "wb") as f:
        f.write(file.file.read())
    out = os.path.join(tmp, "project")
    try:
        with zipfile.ZipFile(zpath) as z:
            z.extractall(out)
    except zipfile.BadZipFile:
        raise HTTPException(400, "That file is not a valid zip archive.")
    entries = [e for e in os.listdir(out) if not e.startswith("__MACOSX")]
    root = os.path.join(out, entries[0]) if len(entries) == 1 and os.path.isdir(os.path.join(out, entries[0])) else out
    return {"project": load(root, os.path.splitext(file.filename)[0])}


class FinishIn(BaseModel):
    name: str


def safe_join(base, rel_path):
    parts = [p for p in rel_path.replace("\\", "/").split("/") if p not in ("", ".")]
    if not parts or ".." in parts:
        raise HTTPException(400, "Invalid file path.")
    return os.path.join(base, *parts)


@app.post("/api/upload/start")
def upload_start():
    if state["tmp"]:
        shutil.rmtree(state["tmp"], ignore_errors=True)
    state["tmp"] = tempfile.mkdtemp(prefix="codelens_")
    os.makedirs(os.path.join(state["tmp"], "project"))
    return {"ok": True}


@app.post("/api/upload/batch")
def upload_batch(files: List[UploadFile] = File(...), paths: str = Form(...)):
    if not state["tmp"]:
        raise HTTPException(400, "Upload was not started.")
    names = json.loads(paths)
    if len(names) != len(files):
        raise HTTPException(400, "Files and paths do not match.")
    base = os.path.join(state["tmp"], "project")
    for f, p in zip(files, names):
        dest = safe_join(base, p)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as out:
            shutil.copyfileobj(f.file, out)
    return {"saved": len(names)}


@app.post("/api/upload/finish")
def upload_finish(body: FinishIn):
    if not state["tmp"]:
        raise HTTPException(400, "Upload was not started.")
    out = os.path.join(state["tmp"], "project")
    entries = os.listdir(out)
    only = os.path.join(out, entries[0]) if len(entries) == 1 else None
    root = only if only and os.path.isdir(only) else out
    return {"project": load(root, body.name)}


@app.post("/api/chat")
def chat(body: ChatIn):
    text = body.message.strip()
    if not text:
        raise HTTPException(400, "Message is empty.")
    try:
        reply = reviewer.chat(text)
    except Exception as e:
        traceback.print_exc()   # full error details appear in the terminal
        raise HTTPException(502, f"The agent failed: {e}")
    if not isinstance(reply, str):
        reply = getattr(reply, "content", str(reply))

    agent = reviewer.agent
    task = getattr(agent, "last_task", None) or "general"
    seen, sources = set(), []
    for s in getattr(agent, "last_sources", []):
        p = rel(s["path"])
        if p not in seen:
            seen.add(p)
            sources.append(p)

    state["history"].append({"role": "user", "content": text})
    state["history"].append({"role": "assistant", "content": reply, "task": task, "sources": sources})
    return {"reply": reply, "task": task, "sources": sources}


@app.delete("/api/project")
def remove_project():
    reviewer.vector_store = VectorStore()      # empty index
    reviewer.agent.memory.clear()              # forget project + chat
    if state["tmp"]:
        shutil.rmtree(state["tmp"], ignore_errors=True)   # delete uploaded copy
    state.update(project=None, root=None, tmp=None, history=[])
    return {"ok": True}


@app.post("/api/clear")
def clear():
    state["history"] = []
    reviewer.agent.memory.messages = []   # keep project + index, clear only the chat
    return {"ok": True}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
