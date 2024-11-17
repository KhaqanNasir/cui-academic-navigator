import os
import streamlit as st
import pandas as pd
from groq import Groq

# Set up the Groq client and API key
GROQ_API_KEY = "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"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load course data
data_path = '/content/COMSATSDATASET.xlsx'  
courses_df = pd.read_excel(data_path)

# Streamlit UI setup
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .stApp {
        font-family: 'Poppins', sans-serif;
        background-color: #0D0D0D;
        color: #F2DFF2;
    }
    .main-title {
        color: #763DF2;
        font-size: 72px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .tagline {
        color: #F2DFF2;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
    }
    .section-header {
        color: #763DF2;
        font-size: 36px;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 20px;
        text-align: center;
    }
    .tips-section {
        margin-top: 30px;
        color: #FFFFFF;
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    load_css()
    
    # Page Title
    st.markdown("<h1 class='main-title'>📘 Personalized Study Plan Generator</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tagline'>Trained on the CDF of COMSATS Courses</p>", unsafe_allow_html=True)

    # Course Selection
    st.markdown("<h2 class='section-header'>🎯 Select Your Exam Details</h2>", unsafe_allow_html=True)
    course_name = st.selectbox("Select Course", courses_df['Subject Name'].unique())
    exam_type = st.selectbox("Choose Exam Type", ["Midterm", "Final Term", "Quiz"])

    # Custom syllabus entry
    syllabus = ""
    if st.checkbox("Enter specific syllabus topics covered (optional):"):
        syllabus = st.text_area("Enter topics covered for your chosen exam:", placeholder="e.g., OS Introduction, CPU Scheduling")

    # Recommendation input to generate the study plan for full marks
    goal_input = st.text_input("To secure full marks, generate a study plan accordingly.")

    # User inputs for study plan
    total_days = st.number_input("📅 Number of days to prepare:", min_value=1, max_value=365, step=1)
    hours_per_day = st.number_input("⏰ Hours available per day:", min_value=1, max_value=24, step=1)

    # Study plan generation
    if st.button("Generate My Study Plan"):
        # Prepare the prompt for the chatbot
        prompt = (
            f"You are a personalized study assistant chatbot. The user aims to secure full marks in a {exam_type} exam for {course_name}. "
            f"The syllabus topics include: '{syllabus}' if provided. They have {total_days} days to prepare, dedicating {hours_per_day} hours per day. "
            f"Based on this, create a detailed study plan that focuses on achieving full marks, incorporating top study strategies and resources. "
            f"Include links to high-quality YouTube channels, official documentation, and any other materials that could best support this goal."
        )

        # Get response from Llama model via Groq API
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192"
            )
            study_plan = response.choices[0].message.content
            st.markdown("<h3 style='color: #4A90E2;'>Your Study Plan for Securing Full Marks</h3>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size: 18px; line-height: 1.6; color: #333;'>{study_plan}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error("An error occurred while fetching the study plan. Please try again later.")

    # Top Recommended Resources
    st.markdown("<h2 class='section-header'>📚 Top Resources for Full Marks Preparation</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        - [Apna College YouTube Channel](https://www.youtube.com/c/ApnaCollegeOfficial) - Programming and core computer science topics in Hindi.
        - [Code with Harry YouTube Channel](https://www.youtube.com/c/CodeWithHarry) - Tutorials on various languages and development topics in Hindi.
        - [Gate Smasher YouTube Channel](https://www.youtube.com/c/GateSmasher) - Covers key subjects like OS and DBMS in-depth.
        - [Geeks for Geeks](https://www.geeksforgeeks.org/) - Articles, coding problems, and interview prep content.
        - [W3 Schools](https://www.w3schools.com/) - Beginner-friendly documentation on HTML, CSS, and more.
        - [Khan Academy](https://www.khanacademy.org/) - Free learning platform for core subjects.
        - [YouTube](https://www.youtube.com) - Search specific topics for additional resources.
        """,
        unsafe_allow_html=True
    )

    # Additional Tips Section
    st.markdown("<h2 class='section-header'>💡 Additional Study Tips</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="tips-section">
        - Create a distraction-free study zone. <br>
        - Use active recall and spaced repetition techniques. <br>
        - Practice with past papers or mock tests. <br>
        - Maintain a healthy balance between study and rest. <br>
        - Stay hydrated and eat nutritious meals for optimal focus. <br>
        - Track your progress and adjust your study plan if needed.
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    st.set_page_config(
        page_title="COMSATS Chatbot",
        page_icon="🎓",
        layout="wide",  # Wide layout for better presentation
        initial_sidebar_state="collapsed"
    )
    main()
