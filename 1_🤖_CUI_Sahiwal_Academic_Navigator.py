import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="CUI Sahiwal Academic Navigator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Poppins font
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    /* Apply Poppins font to the entire app */
    body {
        font-family: 'Poppins', sans-serif;
    }

    /* Header styles */
    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: 600;
        color: #ffffff;
    }

    /* Tagline */
    .tagline {
        text-align: center;
        font-size: 20px;
        font-weight: 400;
        color: #d1d1d1;
    }

    /* Feature Box */
    .feature-box {
        background-color: #212121;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        color: #d1d1d1;
    }

    .feature-title {
        font-size: 22px;
        font-weight: 600;
        color: #007bff;
    }

    .feature-description {
        font-size: 16px;
    }

    /* Button styles */
    .app-button {
        display: inline-block;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: 600;
        text-decoration: none;
        border-radius: 25px;
        margin: 10px;
        transition: all 0.3s ease;
        color: white;
    }

    /* Button hover effect */
    .app-button:hover {
        transform: scale(1.1);
        background-color: #0056b3;
    }

    .blue-btn {
        background-color: #007bff;
    }

    .green-btn {
        background-color: #28a745;
    }

    .yellow-btn {
        background-color: #ffc107;
    }

    .purple-btn {
        background-color: #6f42c1;
    }

    .red-btn {
        background-color: #fd7e14;
    }

    .dark-btn {
        background-color: #343a40;
    }

    /* Intro Statement */
    .intro-statement {
        background-color: #333;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        color: #d1d1d1;
        text-align: center;
        font-size: 18px;
    }

    </style>
    """, unsafe_allow_html=True)

# Main Page Layout
def main():
    load_css()

    # Title and Logo
    st.markdown("<h1 class='main-title'>🤖 CUI Sahiwal Academic Navigator</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tagline'>Your one-stop AI-powered assistant for academic success and campus insights! 🎓✨</p>", unsafe_allow_html=True)
    
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
        <div class='feature-box'>
            <p class='feature-title'>{feature['title']}</p>
            <p class='feature-description'>{feature['description']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Navigation Buttons
    st.markdown("<h2 style='text-align:center; font-family:Poppins;'>🚀 Explore Our Chatbots</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;'>
        <a href="/Personalized_Study_Bot" class="app-button blue-btn">📘 Study Chatbot</a>
        <a href="/Study_Notes_Maker" class="app-button green-btn">📝 Notes Maker</a>
        <a href="/Campus_Insight_AI" class="app-button yellow-btn">🤖 Campus Insights</a>
        <a href="/Multilingual_TTS_Chatbot" class="app-button purple-btn">🎙️ TTS Chatbot</a>
        <a href="/PPT_Generator" class="app-button red-btn">📊 Presentation Generator</a>
        <a href="/CV_Analysis" class="app-button dark-btn">📄 CV Analysis</a>
        <a href="/About_Us" class="app-button dark-btn">👤 About Us</a>
    </div>
    """, unsafe_allow_html=True)

    # Intro Statement
    st.markdown("""
    <div class='intro-statement'>
        <p>📢 Welcome to the CUI Sahiwal Academic Navigator! This AI-powered platform is designed to help you succeed academically by offering personalized study plans, automated tools, and campus insights. Explore now and unlock your full potential! 🚀</p>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.success("Select a page above.")

# Run App
if __name__ == "__main__":
    main()
