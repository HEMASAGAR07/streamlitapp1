import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
from keys import api_key
genai.configure(api_key=api_key)



# Function to read text from PDF
def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to read text from DOCX
def read_docx(file):
    doc = Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

# Function to summarize and extract details from the research papers
def analyze_papers(texts):
    model = genai.GenerativeModel('gemini-pro')

    summaries = []
    for i, text in enumerate(texts):
        prompt = f"Extract the following details from this research paper: {text}\n" \
                 "Title of the paper, Authors of the paper, Algorithms used, Methodology used, Dataset used, Accuracy of the paper, Challenges faced, Optimization function used"
        response = model.generate_content(prompt)
        summaries.append(response.text)

    return summaries

# Streamlit UI for the literature review page
def literature_review_ui():
    st.title("Literature Review")

    num_papers = st.selectbox("Select the number of papers to review:", [1, 2, 3, 4], index=0)

    upload_or_link = st.radio("Select input method:", ("Upload", "Link"))

    if upload_or_link == "Upload":
        uploaded_files = [st.file_uploader(f"Upload Paper {i + 1}", type=["pdf", "docx"]) for i in range(num_papers)]

        if all(uploaded_files):
            texts = []
            for uploaded_file in uploaded_files:
                if uploaded_file.type == "application/pdf":
                    text = read_pdf(uploaded_file)
                elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    text = read_docx(uploaded_file)
                texts.append(text)

            if texts:
                results = analyze_papers(texts)
                for i, result in enumerate(results):
                    st.write(f"**Paper {i + 1} Analysis:**")
                    st.write(result)

    elif upload_or_link == "Link":
        st.write("Currently, URL handling is not implemented. Please use the upload option.")
