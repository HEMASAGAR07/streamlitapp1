import streamlit as st
import google.generativeai as genai
from keys import api_key
genai.configure(api_key=api_key)

# Function to paraphrase text
def paraphrase_text(text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Paraphrase the following text to remove plagiarism:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI for the paraphrasing page
def paraphrasing_ui():
    st.title("Paraphrasing Tool")

    # Input text
    text_input = st.text_area("Enter your text (up to 200 words):", height=200)

    if len(text_input.split()) > 200:
        st.warning("Please limit your text to 200 words.")
    else:
        if st.button("Paraphrase"):
            # Paraphrase the input text
            paraphrased_text = paraphrase_text(text_input)
            st.subheader("Paraphrased Text:")
            st.write(paraphrased_text)

            # Re-paraphrase button
            if st.button("Re-paraphrase"):
                paraphrased_text = paraphrase_text(text_input)
                st.subheader("New Paraphrased Text:")
                st.write(paraphrased_text)
