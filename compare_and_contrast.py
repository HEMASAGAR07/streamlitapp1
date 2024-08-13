import streamlit as st
import google.generativeai as genai
import pandas as pd
from bs4 import BeautifulSoup
import requests
from PyPDF2 import PdfReader
import docx  # Make sure to have python-docx installed
from keys import api_key
genai.configure(api_key=api_key)

# Function to read text from an uploaded file
def read_uploaded_file(file):
    if file.type == "text/plain":
        return file.read().decode("utf-8")
    elif file.type == "application/pdf":
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    else:
        st.error("Unsupported file type.")
        return None

# Function to fetch text content from a URL
def fetch_paper_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    return text

# Function to summarize and compare research papers
def summarize_and_compare_papers(texts):
    summaries = []
    for i, text in enumerate(texts):
        prompt = f"Summarize the following research paper in a simple and clear manner: {text}"
        model = genai.GenerativeModel('gemini-pro')
        summary = model.generate_content(prompt).text
        summaries.append(summary)

    # Prepare comparison prompt
    comparison_prompt = f"Compare the following research papers:\n"
    for i, summary in enumerate(summaries):
        comparison_prompt += f"Paper {i + 1} Summary: {summary}\n"
    comparison = model.generate_content(comparison_prompt).text

    return summaries, comparison

# Function to format output with bold headings
def format_output(summaries, comparison):
    formatted_summaries = []
    for i, summary in enumerate(summaries):
        formatted_summary = f"**Summary of Paper {i + 1}:**\n{summary}"
        formatted_summaries.append(formatted_summary)

    formatted_comparison = f"**Comparison of Papers:**\n{comparison}"

    return formatted_summaries, formatted_comparison

# Function to display the Compare and Contrast UI
def compare_and_contrast_ui():
    st.title("Research Paper Comparison")

    # Ask user how many papers to compare
    num_papers = st.number_input("How many papers do you want to compare?", min_value=1, max_value=5, step=1)

    # User selection: upload files or provide URLs
    option = st.radio("How would you like to provide the research papers?", ("Upload Files", "Provide URLs"))

    texts = []
    if option == "Upload Files":
        for i in range(num_papers):
            uploaded_file = st.file_uploader(f"Upload Research Paper {i + 1}", type=["txt", "pdf", "docx"])
            if uploaded_file:
                text = read_uploaded_file(uploaded_file)
                if text:
                    texts.append(text)

    elif option == "Provide URLs":
        for i in range(num_papers):
            url = st.text_input(f"Enter the URL of Research Paper {i + 1}")
            if url:
                text = fetch_paper_text(url)
                if text:
                    texts.append(text)

    # Summarize and compare papers
    if len(texts) == num_papers and st.button("Compare Papers"):
        summaries, comparison = summarize_and_compare_papers(texts)
        formatted_summaries, formatted_comparison = format_output(summaries, comparison)

        # Display summaries and comparison with better visualization
        for formatted_summary in formatted_summaries:
            st.markdown(formatted_summary)

        st.markdown(formatted_comparison)
