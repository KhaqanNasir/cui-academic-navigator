import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="CUI Sahiwal Academic Navigator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main Page Layout
def main():
    # Title and Logo
    st.markdown("<h1 style='text-align:center; font-family:Poppins;'>🤖 CUI Sahiwal Academic Navigator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-family:Poppins; font-size:20px;'>Your one-stop AI-powered assistant for academic success and campus insights! 🎓✨</p>", unsafe_allow_html=True)
    
    # Logo Section
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("logo.png", width=150, use_column_width=True)
    
    # Features Section
    st.markdown("<h2 style='text-align:center; font-family:Poppins;'>🌟 Features 🌟</h2>", unsafe_allow_html=True)
    features = [
        {
            "title": "📘 Personalized Study Chatbot",
            "description": "Create custom study plans tailored to your syllabus and goals. Ace your exams with ease!"
        },
        {
            "title": "📝 Study Notes Maker",
            "description": "Automatically generate organized notes from your lectures or documents."
        },
        {
            "title": "🤖 Campus Insight AI",
            "description": "Stay updated with campus events, services, and resources to make the most of your university life."
        },
        {
            "title": "🎙️ Multilingual TTS Chatbot",
            "description": "Convert text into speech in multiple languages with customizable voice tones."
        },
        {
            "title": "📊 AI-Powered Presentation Generator",
            "description": "Generate professional and visually appealing presentations effortlessly."
        },
        {
            "title": "📄 CV Analysis Tool",
            "description": "Evaluate CVs and rank candidates based on their skills, experience, and fit."
        },
        {
            "title": "👤 About Us",
            "description": "Learn more about the mission and team behind CUI Sahiwal Academic Navigator."
        }
    ]

    for feature in features:
        st.markdown(f"""
        <div style='background-color:#f8f9fa; border-radius:10px; padding:20px; margin:10px 0; box-shadow:0px 2px 5px rgba(0,0,0,0.1);'>
            <h3 style='font-family:Poppins;'>{feature['title']}</h3>
            <p style='font-family:Poppins; font-size:16px;'>{feature['description']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Navigation Buttons
    st.markdown("<h2 style='text-align:center; font-family:Poppins;'>🚀 Explore Our Chatbots</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;'>
        <a href="/Personalized_Study_Bot" style="display:inline-block; margin:10px; padding:12px 24px; font-family:Poppins; font-size:18px; color:white; background-color:#007bff; border-radius:25px; text-decoration:none;">📘 Study Chatbot</a>
        <a href="/Study_Notes_Maker" style="display:inline-block; margin:10px; padding:12px 24px; font-family:Poppins; font-size:18px; color:white; background-color:#28a745; border-radius:25px; text-decoration:none;">📝 Notes Maker</a>
        <a href="/Campus_Insight_AI" style="display:inline-block; margin:10px; padding:12px 24px; font-family:Poppins; font-size:18px; color:white; background-color:#ffc107; border-radius:25px; text-decoration:none;">🤖 Campus Insights</a>
        <a href="/Multilingual_TTS_Chatbot" style="display:inline-block; margin:10px; padding:12px 24px; font-family:Poppins; font-size:18px; color:white; background-color:#17a2b8; border-radius:25px; text-decoration:none;">🎙️ TTS Chatbot</a>
        <a href="/PPT_Generator" style="display:inline-block; margin:10px; padding:12px 24px; font-family:Poppins; font-size:18px; color:white; background-color:#6f42c1; border-radius:25px; text-decoration:none;">📊 Presentation Generator</a>
        <a href="/CV_Analysis" style="display:inline-block; margin:10px; padding:12px 24px; font-family:Poppins; font-size:18px; color:white; background-color:#fd7e14; border-radius:25px; text-decoration:none;">📄 CV Analysis</a>
        <a href="/About_Us" style="display:inline-block; margin:10px; padding:12px 24px; font-family:Poppins; font-size:18px; color:white; background-color:#343a40; border-radius:25px; text-decoration:none;">👤 About Us</a>
    </div>
    """, unsafe_allow_html=True)

    # Intro Statement
    st.markdown("""
    <div style='background-color:#f8f9fa; border-radius:10px; padding:20px; margin:20px 0;'>
        <p style='font-family:Poppins; font-size:18px; text-align:center;'>📢 Welcome to the CUI Sahiwal Academic Navigator! This AI-powered platform is designed to help you succeed academically by offering personalized study plans, automated tools, and campus insights. Explore now and unlock your full potential! 🚀</p>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.success("Select a page above.")

# Run App
if __name__ == "__main__":
    main()
