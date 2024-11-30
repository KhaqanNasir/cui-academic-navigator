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
    st.markdown("<h1 style='text-align:center;'>🤖 CUI Sahiwal Academic Navigator</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Your AI-Powered Academic Assistant 🎓✨</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("logo.png", width=60, use_column_width=True)

    # Features Section
    st.markdown("<h2 style='text-align:center;'>🌟 Features 🌟</h2>", unsafe_allow_html=True)
    
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
            "description": "Generate speech in your preferred language, voice, and tone! 🌟"
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
            "title": "🎙️ Real Time Voice-to-Voice",
            "description": "Engage in real-time conversations with AI! Upload your voice, get a transcription, and hear the chatbot's response back in voic! 🚀🗣️"
        },
        {
            "title": "👤 About Us",
            "description": "Discover the vision, team, and journey behind this app. Join us on our mission to innovate education! 🌟"
        }
    ]

    for feature in features:
        st.markdown(f"""
        <div style='background-color: #5F6366; padding: 15px; margin: 10px 0; border-radius: 10px;'>
            <h3 style='color: #D3D3D3;'>{feature['title']}</h3>
            <p style='color: #D3D3D3;'>{feature['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        

    # Navigation Buttons
    st.markdown("<h1 style='text-align: center;'>🚀 Explore Our Chatbots</h1>", unsafe_allow_html=True)
    st.markdown("""
      <div style='text-align:center;'>
         <a href="/Personalized_Study_Bot" style="background-color: #007bff; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">📘 Study Chatbot</a>
         <a href="/Study_Notes_Maker" style="background-color: #28a745; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">📝 Study Notes Maker</a>
         <a href="/Campus_Insight_AI" style="background-color: #ffc107; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">🤖 Campus Insight AI</a>
         <a href="/Multilingual_TTS_Chatbot" style="background-color: #6f42c1; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">🎙️ Multilingual TTS Chatbot</a>
         <a href="/PPT_Generator" style="background-color: #fd7e14; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">📊 AI-Powered Presentation Generator</a>
         <a href="/CV_Analysis" style="background-color: #343a40; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">📄 CV Analysis</a>
         <a href="/Real Time Voice-to-Voice" style="background-color: #E10600; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">🎙️ Voice-to-Voice</a>
         <a href="/About_Us" style="background-color: #6c757d; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">👤 About Us</a>
      </div>
     <style>
      @media (max-width: 768px) {
        div {
            text-align: center;
        }
        a {
            display: block;
            margin: 10px auto;
            width: 80%;
            font-size: 16px;
        }
      }
     </style>
    """, unsafe_allow_html=True)


    # Intro Statement
    st.markdown("""
    <div>
        <p style='font-size: 18px; text-align: center;'>📢 Welcome to the CUI Sahiwal Academic Navigator! This AI-powered platform is designed to help you succeed academically by offering personalized study plans, automated tools, and campus insights. Explore now and unlock your full potential! 🚀</p>
    </div>
    """, unsafe_allow_html=True)
    st.sidebar.success("Select a page above.")

# Run App
if __name__ == "__main__":
    main()
