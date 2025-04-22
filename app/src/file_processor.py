# Support for various file formats
import streamlit as st
import os
from typing import Optional
from tests import test_file_ext

class FileProcessor:
    def __init__(self):
        self.file = None
        self.file_type: None
        self.supported_types = {
            ".txt": self._read_txt
        }
        self.content = None

    def upload_file(self) -> None:
        extensions = list(self.supported_types.keys())
        self.file = st.file_uploader(
            "Import your file",
            type=extensions,
            help=f"Supported formats: {', '.join(extensions)}"
        )

        if self.file:
            _, ext = os.path.splitext(self.file.name)
            self.file_type = ext.lower()

    def _read_txt(self) -> str:
        return self.file.getvalue().decode("utf-8")

    def get_content(self) -> Optional[str]:
        if not self.file:
            st.warning("No file uploaded!")
            return None

        if self.file_type not in self.supported_types:
            st.error(f"Unsupported file type: {self.file_type}")
            return None

        try:
            self.content = self.supported_types[self.file_type]()
            return self.content
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
            return None

    def getFile(self):
        return self.file
