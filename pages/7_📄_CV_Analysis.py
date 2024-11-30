import pdfplumber
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import streamlit as st
import matplotlib.pyplot as plt
import docx2txt

# Load the pretrained model and tokenizer
model_name = "distilbert-base-uncased"
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=5)

# Function to extract text from a PDF CV
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

# Function to extract text from a Word CV
def extract_text_from_word(docx_path):
    return docx2txt.process(docx_path)

# Function to analyze the CV text and return scores
def analyze_cv_text(cv_text):
    inputs = tokenizer(cv_text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1).numpy()
    return probabilities

# Function to rank candidates based on their CV analysis
def rank_candidates(cv_data):
    all_candidates = []
    for cv in cv_data:
        cv_scores = analyze_cv_text(cv)
        skills_score = cv_scores[0][0] * 100
        experience_score = cv_scores[0][1] * 100
        total_score = (0.5 * skills_score + 0.5 * experience_score)
        all_candidates.append((cv, total_score, skills_score, experience_score))
    return all_candidates

# Function to reset the session state
def reset_state():
    if "uploaded_files" in st.session_state:
        del st.session_state["uploaded_files"]
    if "candidates" in st.session_state:
        del st.session_state["candidates"]
    st.session_state["uploaded_files"] = None
    st.session_state["candidates"] = []

# Streamlit UI configuration
st.set_page_config(page_title="CV Analysis Tool", layout="wide")

# Apply Poppins font via Google Fonts
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stTextInput textarea {
        height: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main heading
st.title("📄 CV Analysis and Candidate Ranking Tool")
st.markdown("Upload your CVs to analyze skills, experience, and identify the best candidate! 🚀")

# "About the Model" Section
st.header("🧠 About the Model")
st.markdown(
    """
    This CV analysis tool uses **DistilBERT**, a transformer-based model trained on text data, to evaluate CVs. 
    The model scores candidates based on their **skills** and **experience**, generating a ranking to help identify the most suitable candidate. 
    It accepts **PDF** and **Word documents**, extracting text and analyzing it to generate meaningful insights. 🎯
    """
)

# CV Upload Section
st.subheader("📂 Upload CVs")
uploaded_files = st.file_uploader(
    "Choose CV files (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True
)

if uploaded_files:
    cvs = []

    # Extract text from uploaded CVs
    with st.spinner("🔍 Extracting text from CVs..."):
        for uploaded_file in uploaded_files:
            if uploaded_file.type == "application/pdf":
                cvs.append(extract_text_from_pdf(uploaded_file))
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                cvs.append(extract_text_from_word(uploaded_file))

    # Rank candidates
    candidates = rank_candidates(cv_data=cvs)

    if candidates:
        st.subheader("📊 Candidates Analysis")
        for index, candidate in enumerate(candidates):
            cv, total_score, skills_score, experience_score = candidate

            st.markdown(
                f"""
                **Candidate {index + 1}:**
                - **Snippet**: {cv[:50]}...
                - **Total Score**: {total_score:.2f}%
                - **Skills Score**: {skills_score:.2f}%
                - **Experience Score**: {experience_score:.2f}%
                """
            )

        # Plot scores
        st.subheader("📈 Comparison of Skills and Experience Scores")
        labels = [f"CV {i + 1}" for i in range(len(candidates))]
        skills_scores = [candidate[2] for candidate in candidates]
        experience_scores = [candidate[3] for candidate in candidates]

        fig, ax = plt.subplots(figsize=(8, 4))
        x = range(len(candidates))
        ax.bar(x, skills_scores, width=0.4, label="Skills", color="blue")
        ax.bar([p + 0.4 for p in x], experience_scores, width=0.4, label="Experience", color="orange")
        ax.set_xticks([p + 0.2 for p in x])
        ax.set_xticklabels(labels)
        ax.legend()
        st.pyplot(fig)

        # Highlight the best candidate
        best_candidate = max(candidates, key=lambda x: x[1])
        st.success(f"🏆 Best Candidate: CV {candidates.index(best_candidate) + 1}")
    else:
        st.error("No valid CVs found. Please upload valid files.")

# Reset button
if st.button("🔄 Clear All"):
    reset_state()
    st.success("All CVs cleared!")
