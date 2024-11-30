import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="CUI Sahiwal Academic Navigator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main Page Layout
def main():
    # Title Section with Grid Layout
    col1, col2 = st.columns([6, 6])
    
    # Left Column: Display Image
    with col1:
        st.image("logo.png", caption="Your Academic Partner", use_column_width=True)
    
    # Right Column: Display Title and Subtitle
    with col2:
        st.markdown("### 🤖 **CUI Sahiwal Academic Navigator**")
        st.markdown("""
        Welcome to the **CUI Sahiwal Academic Navigator** – your personalized AI-powered assistant!  
        Explore cutting-edge tools designed to enhance your academic journey.  
        """)

    st.markdown("---")  # Divider

    # Introduction Section
    st.markdown("### 🌟 **Why Choose These Chatbots?** 🌟")
    st.markdown("""
    These AI-driven tools are developed specifically for students of **CUI, Sahiwal**, providing personalized solutions for academic challenges:  
    - Simplify study planning and note-taking.  
    - Get professional assistance for presentations and CV analysis.  
    - Stay informed with campus updates and more!  
    """)

    st.markdown("---")  # Divider

    # Features Section
    st.markdown("### 🚀 **Chatbot Features**")
    features = [
        {
            "title": "📘 **Personalized Study Chatbot**",
            "description": "Tailored study plans based on your course and exams. Study smarter, not harder! 🕒"
        },
        {
            "title": "📝 **Study Notes Maker**",
            "description": "Effortlessly create structured lecture notes to stay ahead in your studies. 📓"
        },
        {
            "title": "🤖 **Campus Insight AI**",
            "description": "Get campus updates, event details, and services to stay connected! 🎉"
        },
        {
            "title": "🎙️ **Multilingual TTS Chatbot**",
            "description": "Convert text to speech in multiple languages, accents, and tones. Enhance accessibility! 🌍"
        },
        {
            "title": "📊 **AI-Powered Presentation Generator**",
            "description": "Generate professional presentations in seconds for seminars or projects. ✨"
        },
        {
            "title": "📄 **CV Analysis Tool**",
            "description": "Evaluate and optimize CVs with AI for better job applications. 💼"
        }
    ]

    for feature in features:
        st.markdown(f"""
        #### {feature['title']}
        - {feature['description']}
        """)

    st.markdown("---")  # Divider

    # Chatbot Navigation
    st.markdown("### 📌 **Explore the Chatbots**")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("📘 Study Chatbot")
        st.button("🎙️ Multilingual TTS Chatbot")
    with col2:
        st.button("📝 Study Notes Maker")
        st.button("📄 CV Analysis Tool")
    with col3:
        st.button("🤖 Campus Insight AI")
        st.button("📊 Presentation Generator")

    # Additional Section
    st.markdown("### 💡 **How These Chatbots Can Help You**")
    st.markdown("""
    These chatbots are designed to:  
    - Save your time by automating repetitive academic tasks.  
    - Provide personalized assistance tailored to your study needs.  
    - Improve academic efficiency and outcomes.  
    - Enhance accessibility and support in multiple languages.  
    """)

    # Footer
    st.markdown("---")
    st.markdown("""
    🔔 **Ready to explore?**  
    Click on any chatbot above to get started and elevate your academic journey! 🚀  
    """)

    # Sidebar
    st.sidebar.success("Select a chatbot from the list!")

# Run App
if __name__ == "__main__":
    main()
