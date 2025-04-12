import streamlit as st
import time

st.title("AI powered document summary")

file = st.file_uploader("Import your file", type="txt")

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if file is not None and not st.session_state.submitted:
    if st.button("Summarize"):
        st.session_state.submitted = True
        st.rerun()

if st.session_state.submitted:
    with st.spinner("Summarizing your doc...."):
        time.sleep(5)
    st.success("Your summary is ready:")
    st.markdown("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Nulla accumsan, metus ultrices eleifend gravida, nulla nunc varius lectus, 
        nec rutrum justo nibh eu lectus.

        Ut vulputate semper dui. Fusce erat odio, sollicitudin vel erat vel, 
        interdum mattis neque. Substainably deep dive intuitive thinking.
        """)
