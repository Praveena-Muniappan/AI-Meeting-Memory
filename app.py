
import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Meeting Memory",
    page_icon="🧠",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------
st.title("🧠 AI Meeting Memory")
st.write(
    "Upload a meeting recording to generate transcripts, summaries, "
    "action items, and search previous meetings."
)

st.divider()

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select",
    [
        "Upload Meeting",
        "Meeting History",
        "Search Meetings",
        "Settings"
    ]
)

# ----------------------------
# Upload Page
# ----------------------------
if page == "Upload Meeting":

    st.header("Upload Meeting")

    uploaded_file = st.file_uploader(
        "Choose an audio file",
        type=["mp3", "wav", "m4a"]
    )

    if uploaded_file:
        st.success(f"Uploaded: {uploaded_file.name}")

        st.audio(uploaded_file)

        if st.button("Generate Transcript"):
            st.info("Transcription module will be integrated here.")

# ----------------------------
# Meeting History
# ----------------------------
elif page == "Meeting History":

    st.header("Meeting History")

    st.info("Meeting history will be displayed here.")

# ----------------------------
# Search
# ----------------------------
elif page == "Search Meetings":

    st.header("Search Previous Meetings")

    query = st.text_input("Ask a question about past meetings")

    if st.button("Search"):
        st.info("Semantic search will be integrated here.")

# ----------------------------
# Settings
# ----------------------------
else:

    st.header("Settings")

    st.info("API configuration and preferences will be available here.")
