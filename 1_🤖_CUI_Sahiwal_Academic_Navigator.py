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
    # Global CSS to apply the Poppins font
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    html, body, [class*="css"], *{
        font-family: 'Poppins', sans-serif;
    }
    a {
        text-decoration: none;
        font-weight: 500;
        font-family: 'Poppins', sans-serif;
    }
    a:hover {
        opacity:0.7;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    
    # Title and Logo Section
    col1, col2 = st.columns([1, 1])  # Adjust the ratio if needed
    with col1:
       st.markdown("<h1 style='font-size: 50px; margin-top: 20px; font-weight: 1000;'>CUI Sahiwal Academic Navigator</h1>", unsafe_allow_html=True)
       st.markdown("<p style='font-size: 18px; color: gray;'>Your AI-Powered Academic Assistant, designed to help students and educators navigate the academic journey with ease and precision.</p>",
                unsafe_allow_html=True)
       st.markdown("<p style='font-size: 18px; color: gray;'>Providing smart solutions for academic challenges, including personalized study resources, exam preparation, and academic guidance. 🎓✨</p>",
                unsafe_allow_html=True)
       st.markdown("""<ul style='font-size: 18px; color: gray; margin-left: 20px;'>
               <li>🌟 AI-driven academic guidance and support.</li>
               <li>🧠 Tailored recommendations for study resources and exam prep.</li>
               <li>🎓 Empowering students and educators to excel in their academic journey.</li>
               <li>📚 Your one-stop solution for academic success.</li>
           </ul>""", unsafe_allow_html=True)
    with col2:
       st.image("logo.png", width=700)

    st.markdown("<br><br><h3 style='text-align:center; font-size:30px; font-weight:1000;'>Explore More</h3><h3 style='text-align:center;'>⬇️</h3><br><br><br><br><br>", unsafe_allow_html=True)
    

    # Features Section
    st.markdown("<h2 style='text-align:center; font-family: Poppins, sans-serif; font-weight: 600; color: #333;'>🌟 Features 🌟</h2>", unsafe_allow_html=True)

    features = [
        {
        "title": "📘 Personalized Study Chatbot",
        "description": "Get tailored study plans based on your course outline. Make your study time super productive! 🕒"
        },
        {
        "title": "🎙️ Real Time Text-to-Voice",
        "description": "Engage in real-time conversations with AI! Upload your voice, get a transcription, and hear the chatbot's response back in voice! 🚀🗣️"
        },
        {
        "title": "📝 Study Notes Maker",
        "description": "Effortlessly organize and create notes from your lectures or resources. Stay ahead with well-structured notes! 📓"
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
        "title": "🖼️ Profile Pic Generator",
        "description": "Transform your photos effortlessly into 50 unique and stunning profile pictures with various vibrant backgrounds! 🎨✨"
        },
        {
        "title": "👤 About Us",
        "description": "Discover the vision, team, and journey behind this app. Join us on our mission to innovate education! 🌟"
        }
    ]

    for feature in features:
        st.markdown(f"""
        <div style='background-color: #1A1A1A; padding: 25px; margin: 20px 0; border-radius: 12px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);'>
            <h3 style='color: #F0F0F0; font-family: "Poppins", sans-serif; font-weight: 600; font-size: 22px; margin-bottom: 10px;'>
                {feature['title']}
            </h3>
            <p style='color: #B0B0B0; font-family: "Poppins", sans-serif; font-size: 16px; line-height: 1.5;'>
                {feature['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Navigation Buttons
    st.markdown("<h1 style='text-align: center;'>🚀 Explore Our Chatbots</h1>", unsafe_allow_html=True)
    st.markdown("""
      <div style='text-align:center;'>
         <a href="/Personalized_Study_Bot" style="background-color: #007bff; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">📘 Study Chatbot</a>
         <a href="/Real_Time_Text-to-Voice" style="background-color: #ffc107; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">🎙️ Text to Voice</a>
         <a href="/Study_Notes_Maker" style="background-color: #28a745; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">📝 Study Notes Maker</a>
         <a href="/Multilingual_TTS_Chatbot" style="background-color: #6f42c1; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">🎙️ Multilingual TTS Chatbot</a>
         <a href="/PPT_Generator" style="background-color: #fd7e14; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">📊 AI-Powered ppt Generator</a>
         <a href="/CV_Analysis" style="background-color: #343a40; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">📄 CV Analysis</a>
         <a href="/Profile_Pic_Generator" style="background-color: #846141; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">🖼️ Profile Pic Generator</a>
         <a href="/About_Us" style="background-color: #6c757d; color: white; padding: 12px 24px; font-size: 18px; margin: 5px; border-radius: 8px; text-decoration: none; display: inline-block;">👤 About Us</a>
      </div>
    """, unsafe_allow_html=True)

    # Intro Statement
    st.markdown("""
    <div>
        <p style='font-size: 18px; text-align: center;'>📢 Welcome to the CUI Sahiwal Academic Navigator! This AI-powered platform is designed to help you succeed academically by offering personalized study plans, automated tools, and campus insights. Explore now and unlock your full potential! 🚀</p>
    </div>
    """, unsafe_allow_html=True)
    # Footer
    st.markdown("---")
    st.markdown(
      '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2025</p>',
       unsafe_allow_html=True)

    st.sidebar.success("Select a page above.")

# Run App
if __name__ == "__main__":
    main()
