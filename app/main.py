# Main giga kox file
import streamlit as st
import time
from src import FileProcessor, Summarizer
from config.settings import settings

def main():
    st.title("Kaka - AI powered document summary")

    fileProcessor = FileProcessor()
    fileProcessor.upload_file()
    file = fileProcessor.getFile()

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    if file is not None and not st.session_state.submitted:
        if st.button("Summarize"):
            st.session_state.submitted = True
            st.rerun()

    if st.session_state.submitted:
        summarizzler = Summarizer(settings)
        result = summarizzler.summarize(fileProcessor.get_content())
        with st.spinner("Summarizing your doc...."):
            time.sleep(5)
        st.success("Your summary is ready:")
        st.markdown(result)


if __name__ == "__main__":
    main()