import streamlit as st
import time
from src.file_processor import FileProcessor
from src.summarizer import Summarizer
from config.settings import settings, quality, length, language

def main():
    if 'tests_run' not in st.session_state:
        st.session_state.tests_run = False

    if not st.session_state.tests_run:
        st.session_state.tests_run = True

    st.title("Kaka - AI powered document summary")
    sumLenght = st.radio(
        "Summary length",
        ["long", "mid", "short"],
        captions = [
            "approximately 2/3 of the original",
            "approximately 1/2 of the original",
            "approximately 1/3 of the original"
        ],
    )
    sumQuality = st.radio(
        "Summary quality",
        ["excellent", "good", "crapy"],
        captions = [
            "high coherence, accurate, well-structured",
            "average quality, some simplifications allowed",
            "intentionally lower quality, possibly missing key points or slightly incoherent"
        ],
    )

    sumLang = st.selectbox(
        "Summary language",
        ["Polish", "English", "German", "French", "Japanese", "Spanish", "Danish", "Chinese"],
    )

    download_format = st.radio(
            "Select download format",
            ["Text File (.txt)", "Word Document (.docx)"]
        )

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
        result = summarizzler.summarize(fileProcessor.get_content(), length[sumLenght], quality[sumQuality], language[sumLang])
        with st.spinner("Summarizing your doc...."):
            time.sleep(1)
        st.success("Your summary is ready:")
        st.markdown(result)

        if download_format == "Text File (.txt)":
            st.download_button(
                label="Download summary",
                data=result,
                file_name="summary.txt",
                mime="text/plain"
            )

        elif download_format == "Word Document (.docx)":
            from io import BytesIO
            from docx import Document
            
            doc = Document()
            doc.add_paragraph(result)
            buffer = BytesIO()
            doc.save(buffer)
            buffer.seek(0)
            
            st.download_button(
                label="Download summary",
                data=buffer,
                file_name="summary.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

    
if __name__ == "__main__":
    main()