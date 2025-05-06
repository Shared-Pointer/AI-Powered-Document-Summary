# Main giga kox file
import streamlit as st
import time
from src import FileProcessor, Summarizer
from config.settings import settings

def main():
    if 'tests_run' not in st.session_state:
        st.session_state.tests_run = False

    if not st.session_state.tests_run:
        # test_http.test_port()
        # test_file_ext.test_file_ext("manu.txt")
        # test_file_ext.test_file_ext("manu.pdf")
        st.session_state.tests_run = True

    st.title("Kaka - AI powered document summary")

    fileProcessor = FileProcessor()
    fileProcessor.upload_file()
    file = fileProcessor.getFile()

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    if file is not None and not st.session_state.submitted:
        # test_file.test_file_name(file)
        if st.button("Summarize"):
            st.session_state.submitted = True
            st.rerun()

    if st.session_state.submitted:
        summarizzler = Summarizer(settings)
        result = summarizzler.summarize(fileProcessor.get_content())
        with st.spinner("Summarizing your doc...."):
            time.sleep(1)
        st.success("Your summary is ready:")
        st.markdown(result)


if __name__ == "__main__":
    main()