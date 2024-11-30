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
    st.title("🤖 CUI Sahiwal Academic Navigator")
    st.markdown("### Your AI-Powered Academic Assistant 🎓✨")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("logo.png", width=60, use_column_width=True)

    # Features Section
    st.header("🌟 Features 🌟")
    features = [
        {
            "title": "📘 Personalized Study Chatbot",
            "description": "Get tailored study plans based on your course outline. Make your study time super productive! 🕒"
        },
        {
            "title": "📝 Study Notes Maker",
            "description": "Effortlessly organize and create notes from your lectures or resources. Stay ahead with well-structured notes! 📓"
        },
        {
            "title": "🤖 Campus Insight AI",
            "description": "Learn about campus details, events, and services. Stay informed and connected! 🎉"
        },
        {
            "title": "🎙️ Multilingual TTS Chatbot",
            "description": "Generate speech in your preferred language, voice, and tone.! 🌟"
        },
        {
            "title": "📊 AI-Powered Presentation Generator",
            "description": "Create professional presentations effortlessly with AI-powered content and formatting! 📊✨"
        },
        {
            "title": "📄 CV Analysis",
            "description": "Analyze CVs effortlessly with AI to rank candidates based on skills and experience, helping you find the best fit for the job! 📄🤖"
        },
        {
            "title": "👤 About Us",
            "description": "Discover the vision, team, and journey behind this app. Join us on our mission to innovate education! 🌟"
        }
    ]

    for feature in features:
        st.subheader(feature['title'])
        st.write(feature['description'])

    # Navigation Buttons
    st.header("🚀 Explore Our Chatbots")
    st.markdown("""
    <div style='text-align:center;'>
        <a href="/Personalized_Study_Bot" class="stButton">📘 Study Chatbot</a>
        <a href="/Study_Notes_Maker" class="stButton">📝 Study Notes Maker</a>
        <a href="/Campus_Insight_AI" class="stButton">🤖 Campus Insight AI</a>
        <a href="/Multilingual_TTS_Chatbot" class="stButton">🎙️ Multilingual TTS Chatbot</a>
        <a href="/PPT_Generator" class="stButton">📊 AI-Powered Presentation Generator</a>
        <a href="/CV_Analysis" class="stButton">📄 CV Analysis</a>
        <a href="/About_Us" class="stButton">👤 About Us</a>
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
