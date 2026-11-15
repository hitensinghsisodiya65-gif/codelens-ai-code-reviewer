import streamlit as st

from main import CodeReviewer


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖"
)


# =========================
# Title
# =========================

st.title("🤖 AI Code Reviewer")

st.write(
    "Upload your code project and ask questions about it."
)


# =========================
# Create CodeReviewer
# =========================

if "reviewer" not in st.session_state:

    st.session_state.reviewer = CodeReviewer()


reviewer = st.session_state.reviewer


# =========================
# Project Upload
# =========================

project_path = st.text_input(
    "Enter project path"
)


if st.button("Load Project"):

    if project_path:

        with st.spinner(
            "Analyzing project..."
        ):

            reviewer.load_project(
                project_path
            )

        st.success(
            "Project loaded successfully!"
        )

    else:

        st.warning(
            "Please enter project path"
        )


# =========================
# Chat Section
# =========================

st.divider()

st.subheader(
    "Ask your AI Assistant"
)


query = st.chat_input(
    "Ask about your code..."
)


if query:

    with st.chat_message("user"):

        st.write(query)


    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            response = reviewer.chat(
                query
            )

        st.write(response)