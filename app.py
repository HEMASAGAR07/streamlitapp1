import streamlit as st
from compare_and_contrast import compare_and_contrast_ui
from literature_review import literature_review_ui
from paraphrasing import paraphrasing_ui

def main():
    # Header
    st.markdown("""
        <style>
        .header { 
            padding: 10px; 
            background-color: #f0f2f6; 
            text-align: center; 
            border-bottom: 1px solid #d0d0d0; 
        }
        .header h1 { 
            margin: 0; 
            color: #333; 
        }
        </style>
        <div class="header">
            <h1>Research Tools Suite</h1>
        </div>
        """, unsafe_allow_html=True)

    # Sidebar
    st.sidebar.title("Navigation")
    st.sidebar.image("https://cdn-icons-png.freepik.com/256/2082/2082022.png?semt=ais_hybrid", width=150)  # Add your logo here
    st.sidebar.markdown("---")

    # Sidebar: Show all tools
    app_mode = st.sidebar.selectbox("Choose a tool:",
                                    ["Compare and Contrast",
                                     "Literature Review",
                                     "Paraphrasing"])

    # Main Content
    st.markdown("""
        <style>
        .main-content { 
            padding: 20px; 
            background-color: #ffffff; 
            border-radius: 8px; 
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
        }
        </style>
        <div class="main-content">
        """, unsafe_allow_html=True)

    if app_mode == "Compare and Contrast":
        st.subheader("Compare and Contrast Tool")
        st.markdown("""
            Use this tool to compare and contrast different research papers. 
            Upload files or provide URLs for analysis.
        """)
        compare_and_contrast_ui()

    elif app_mode == "Literature Review":
        st.subheader("Literature Review Tool")
        st.markdown("""
            Review and extract detailed information from research papers. 
            Upload papers in PDF or DOCX format.
        """)
        literature_review_ui()

    elif app_mode == "Paraphrasing":
        st.subheader("Paraphrasing Tool")
        st.markdown("""
            Paraphrase your text to remove plagiarism. 
            Enter your text (up to 200 words) and get a paraphrased version.
        """)
        paraphrasing_ui()

    st.markdown("</div>", unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <style>
        .footer { 
            padding: 10px; 
            background-color: #f0f2f6; 
            text-align: center; 
            border-top: 1px solid #d0d0d0; 
            margin-top: 20px;
        }
        .footer p { 
            margin: 0; 
            color: #777; 
        }
        </style>
        <div class="footer">
            <p>© 2024 Your Company. All Rights Reserved.</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
