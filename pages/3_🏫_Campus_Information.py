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
    st.title("🏫 COMSATS University Islamabad, Sahiwal Campus Chatbot")
    
    # Display instructions for the user
    st.write("Ask any questions related to COMSATS University Islamabad, Sahiwal Campus facilities, events, or departments.")
    
    # Initialize chat history and clear button functionality
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    
    user_question = st.text_input("Enter your question about the campus:")
    
    if st.button("Ask"):
        # Step 1: Retrieve data
        relevant_data = fetch_university_data(user_question)
        
        st.session_state["chat_history"].append({"role": "user", "content": user_question})
        st.session_state["chat_history"].append({"role": "assistant", "content": relevant_data})

        st.markdown("#### Answer:")
        st.write(relevant_data)

    # Display chat history
    st.markdown("### 💬 Chat History")
    for message in st.session_state["chat_history"]:
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**Bot:** {message['content']}")

    # Clear chat history button
    if st.button("Clear Chat History"):
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
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
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

# Run the app with proper configuration
if __name__ == "__main__":
    main()
