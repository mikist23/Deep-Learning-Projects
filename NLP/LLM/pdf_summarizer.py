import streamlit as st
import os

st.set_page_config(page_title="PDF Summarizer")
st.title("PDF Summarizer")
st.write("Summarize your PDF files using the power of LLMs")
st.divider()

pdf = st.file_uploader("Upload your PDF", type="pdf")
submit = st.button("Generate Summary")

