import streamlit as st
import requests
from bs4 import BeautifulSoup

# Set the page config at the very beginning of the script
st.set_page_config(
    page_title="COMSATS Chatbot",
    page_icon="🎓",
    layout="wide",  # Wide layout for better presentation
    initial_sidebar_state="collapsed"
)

# URLs for fetching data
facebook_url = "https://www.facebook.com/comsats.sahiwal?mibextid=ZbWKwL"
instagram_url = "https://www.instagram.com/cui_sahiwal/"
website_url = "https://www.sahiwal.comsats.edu.pk/"
linkedin_url = "https://www.linkedin.com/company/cui-sahiwal-campus/mycompany/verification/"

# Function to fetch data from the university website
def fetch_university_data(query):
    # Replace with the URL of the website you want to scrape
    urls = [website_url, facebook_url, instagram_url, linkedin_url]
    relevant_info = ""
    
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx/5xx responses
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Scrape the website for relevant content
            content = soup.find_all("p")  # This will find all <p> tags on the page
            info = " ".join([p.get_text() for p in content if query.lower() in p.get_text().lower()])
            
            if info:
                relevant_info += f"\nFrom {url}: \n{info}\n"
        except requests.exceptions.RequestException as e:
            relevant_info += f"Error fetching data from {url}: {e}\n"
    
    if relevant_info:
        return relevant_info
    else:
        return "Sorry, I couldn't find relevant information on the websites. Please try another query."

# Define the main function for the Streamlit app
def main():
    st.markdown('<h1 class="main-title">🏫 COMSATS University Islamabad, Sahiwal Campus Chatbot</h1>', unsafe_allow_html=True)
    
    # Display instructions for the user
    st.markdown('<p class="intro-statement">Ask any questions related to COMSATS University Islamabad, Sahiwal Campus facilities, events, or departments.</p>', unsafe_allow_html=True)
    
    # Initialize chat history and clear button functionality
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    
    user_question = st.text_input("Enter your question about the campus:", key="user_question", label_visibility="collapsed")
    
    if st.button("Ask", key="ask_button"):
        # Step 1: Retrieve data
        relevant_data = fetch_university_data(user_question)
        
        # Update chat history
        st.session_state["chat_history"].append({"role": "user", "content": user_question})
        st.session_state["chat_history"].append({"role": "assistant", "content": relevant_data})

        st.markdown("#### Answer:")
        st.write(relevant_data)

    # Display chat history with better styling
    st.markdown('<h3 class="section-header">💬 Chat History</h3>', unsafe_allow_html=True)
    for message in st.session_state["chat_history"]:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot-message"><strong>Bot:</strong> {message["content"]}</div>', unsafe_allow_html=True)

    # Clear chat history button
    if st.button("Clear Chat History", key="clear_history_button"):
        st.session_state["chat_history"].clear()
        st.success("Chat history cleared.")

# Add custom styling for the UI
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
        margin-top: 50px;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .intro-statement {
        background-color: #421E59;
        border-radius: 10px;
        padding: 20px;
        margin: 30px 0;
        text-align: center;
        font-size: 18px;
        color: #F2DFF2;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .chat-message {
        margin-bottom: 15px;
        padding: 10px;
        border-radius: 10px;
    }
    .user-message {
        background-color: #5129A6;
        color: #F2DFF2;
        text-align: left;
    }
    .bot-message {
        background-color: #763DF2;
        color: #F2DFF2;
        text-align: right;
    }
    .button-container {
        text-align: left;
        margin-top: 20px;
    }
    .section-header {
        color: #763DF2;
        font-size: 36px;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 20px;
        text-align: left;
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
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Run the app with proper configuration
if __name__ == "__main__":
    main()
