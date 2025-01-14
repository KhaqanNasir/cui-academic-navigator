import os
import streamlit as st
import pandas as pd
from groq import Groq

# Set up Streamlit page config (must be the first Streamlit command)
st.set_page_config(
    page_title="Personalized Study Plan Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Retrieve Groq API key securely from Streamlit secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY2"])

# Load course data
data_path = os.path.join(os.path.dirname(__file__), 'assets', 'COMSATSDATASET.xlsx')  
courses_df = pd.read_excel(data_path)

# Global font setup
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    .stApp {
        font-family: 'Poppins', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Main function for the Streamlit app
def main():
    # Page Title
    st.title("📚 Personalized Study Plan Generator")
    st.write("Trained on the **CDF of COMSATS Courses**, this chatbot helps you create a detailed study plan tailored to your needs.")

    # Course Selection
    st.header("🎯 Select Your Exam Details")
    course_name = st.selectbox("📚 Select Course", courses_df['Subject Name'].unique())
    exam_type = st.selectbox("📝 Choose Exam Type", ["Midterm", "Final Term", "Quiz"])

    # Custom syllabus entry
    st.subheader("📋 Enter Specific Syllabus Topics (Optional)")
    syllabus = st.text_area("Enter topics covered for your chosen exam:", placeholder="E.g., OS Introduction, CPU Scheduling")

    # User inputs for study plan
    st.subheader("🔧 Customize Your Study Plan")
    total_days = st.number_input("📅 Number of Days to Prepare:", min_value=1, max_value=365, step=1)
    hours_per_day = st.number_input("⏰ Hours Available per Day:", min_value=1, max_value=24, step=1)
    goal_input = st.text_input("🏆 Your Goal (e.g., Secure Full Marks):")

    # Generate Study Plan
    if st.button("Generate My Study Plan 🧠"):
        if not goal_input.strip():
            st.warning("⚠️ Please provide a goal for better plan generation!")
        else:
            # Prepare the prompt for Groq
            prompt = (
                f"You are a personalized study assistant chatbot. The user aims to secure full marks in a {exam_type} exam for {course_name}. "
                f"The syllabus topics include: '{syllabus}' (if provided). They have {total_days} days to prepare, dedicating {hours_per_day} hours per day. "
                f"Create a detailed study plan that incorporates top strategies, resources (e.g., YouTube channels, documentation), and actionable advice."
            )

            # Fetch response from the model
            try:
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama3-8b-8192"
                )
                study_plan = response.choices[0].message.content
                st.header("📖 Your Study Plan")
                st.write(study_plan)
            except Exception as e:
                st.error("❌ An error occurred while generating your study plan. Please try again later.")
    
    # Display Recommended Resources
    st.header("📚 Top Resources for Preparation")
    st.write(
        """
        - [📺 Apna College YouTube Channel](https://www.youtube.com/c/ApnaCollegeOfficial) - Programming and core computer science topics.
        - [📺 Code with Harry](https://www.youtube.com/c/CodeWithHarry) - Tutorials on various languages and development topics.
        - [📺 Gate Smasher](https://www.youtube.com/c/GateSmasher) - Key subjects like OS and DBMS explained in-depth.
        - [🌐 Geeks for Geeks](https://www.geeksforgeeks.org/) - Coding problems, articles, and interview prep content.
        - [🌐 W3 Schools](https://www.w3schools.com/) - Beginner-friendly documentation on HTML, CSS, and more.
        - [🌐 Khan Academy](https://www.khanacademy.org/) - Free platform for core subjects.
        """
    )

    # Additional Study Tips
    st.header("💡 Study Tips for Success")
    st.write(
        """
        - Create a distraction-free study zone.  
        - Use active recall and spaced repetition.  
        - Practice with past papers or mock tests.  
        - Maintain a balance between study and rest.  
        - Stay hydrated and eat healthy meals for focus.  
        - Track your progress and adjust your plan as needed.
        """
     )
 # Footer
    st.markdown("---")
    st.markdown(
      '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2025</p>',
       unsafe_allow_html=True)

if __name__ == "__main__":
    main()

