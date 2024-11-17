import streamlit as st

st.set_page_config()

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    .stApp {
        background-color: #0D0D0D;
        font-family: 'Poppins', sans-serif;
    }
    .main-title {
        color: #763DF2;
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .tagline {
        color: #5129A6;
        font-size: 28px;
        font-style: italic;
        text-align: center;
        margin-bottom: 30px;
    }
    .logo-container {
        text-align: center;
        margin: 20px 0;
    }
    .section-header {
        color: #763DF2;
        font-size: 36px;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 20px;
        text-align: center;
    }
    .feature-box {
        background-color: #421E59;
        border-radius: 15px;
        padding: 20px;
        margin: 20px auto;
        width: 90%;
        max-width: 700px;
        transition: transform 0.3s ease-in-out;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .feature-box:hover {
        transform: scale(1.03);
        background-color: #5129A6;
    }
    .feature-title {
        color: #F2DFF2;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .feature-description {
        color: #F2DFF2;
        font-size: 16px;
        margin-bottom: 10px;
    }
    .app-button {
        background-color: #5129A6;
        color: #F2DFF2;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 25px;
        text-align: center;
        margin: 10px;
        display: inline-block;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .app-button:hover {
        background-color: #763DF2;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .intro-statement {
        background-color: #421E59;
        border-radius: 10px;
        padding: 20px;
        margin: 30px 0;
        text-align: center;
        font-size: 18px;
        color: #F2DFF2;
    }
    p {
        color: #F2DFF2;
    }
    </style>
    """, unsafe_allow_html=True)

# Main Page Layout
def main():
    load_css()

    # Title and Logo
    st.markdown("<h1 class='main-title'>📚 COMSATS University Islamabad, Sahiwal Campus 🤖</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tagline'>Your AI-Powered Academic Assistant 🎓✨</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.image("logo.png", width=120, use_column_width=True)

    # Features Section
    st.markdown("<h2 class='section-header'>🌟 Features 🌟</h2>", unsafe_allow_html=True)
    features = [
    {
        "title": "📘 Personalized Study Chatbot",
        "description": "Get tailored study plans based on your course outline. Make your study time super productive! 🕒"
    },
    {
        "title": "📝 Notes Maker",
        "description": "Effortlessly organize and create notes from your lectures or resources. Stay ahead with well-structured notes! 📓"
    },
    {
        "title": "🏫 Campus Information Chatbot",
        "description": "Learn about campus details, events, and services. Stay informed and connected! 🎉"
    },
    {
        "title": "👤 About Us",
        "description": "Discover the vision, team, and journey behind this app. Join us on our mission to innovate education! 🌟"
    }
]

    for feature in features:

     st.markdown(f"""
       <div class='feature-box'>
        <p class='feature-title'>{feature['title']}</p>
        <p>{feature['description']}</p>
      </div>
     """, unsafe_allow_html=True)


    # Navigation Buttons
    st.markdown("<h2 class='section-header'>🚀 Explore Our Chatbots</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;'>
        <a href="/Personalized_Study_Bot" class="app-button">📘 Study Chatbot</a>
        <a href="/Notes_Maker" class="app-button">📝 Notes Maker</a>
        <a href="/Campus_Information" class="app-button">🏫 Campus Info</a>
        <a href="/About_Us.py" class="app-button">👤 About Us</a>
    </div>
    """, unsafe_allow_html=True)

    # Intro Statement
    st.markdown("""
    <div class='intro-statement'>
        <p>📢 Welcome to the COMSATS University chatbot! We are here to assist students with personalized study plans, campus details, and more. Start exploring now! 🚀</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.success("Select a above page")

# Run App
if __name__ == "__main__":
    st.set_page_config(
        page_title="COMSATS Chatbot",
        page_icon="🎓",
        layout="wide", 
        initial_sidebar_state="collapsed"
    )
    main()
