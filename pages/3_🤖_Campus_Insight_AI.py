import streamlit as st
import requests
from bs4 import BeautifulSoup

# Set the page config at the very beginning of the script
st.set_page_config(
    page_title="Campus Insight AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# URLs for fetching data
facebook_url = "https://www.facebook.com/comsats.sahiwal?mibextid=ZbWKwL"
instagram_url = "https://www.instagram.com/cui_sahiwal/"
website_url = "https://www.sahiwal.comsats.edu.pk/"
linkedin_url = "https://www.linkedin.com/company/cui-sahiwal-campus/mycompany/verification/"

# Function to fetch data from websites with enhanced scraping
def fetch_university_data(query):
    urls = [website_url, facebook_url, instagram_url, linkedin_url]
    relevant_info = ""
    
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Scrape both <p> and <div> tags for better data coverage
            content = soup.find_all(["p", "div"])
            info = " ".join([tag.get_text(strip=True) for tag in content if query.lower() in tag.get_text(strip=True).lower()])
            
            if info:
                relevant_info += f"\n🔗 **From {url}**:\n{info}\n"
        except requests.exceptions.RequestException as e:
            relevant_info += f"❌ Error fetching data from {url}: {e}\n"
    
    if relevant_info.strip():
        return relevant_info
    else:
        return "⚠️ Sorry, I couldn't find relevant information on the websites. Please try another query or refine your search."

# Main function for Streamlit app
def main():
    st.markdown("<h1 style='text-align: center;'>🤖 Campus Insight AI</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Get quick and accurate insights about COMSATS University Islamabad, Sahiwal Campus.</p>",
        unsafe_allow_html=True
    )

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Input field for user's question
    user_question = st.text_input(
        "🔍 Ask a question about the campus:",
        key="user_question",
        placeholder="E.g., What programs does the university offer?",
        label_visibility="collapsed"
    )

    # Button to process the user's query
    if st.button("Ask 🤔", key="ask_button"):
        if user_question.strip():
            # Fetch relevant data
            relevant_data = fetch_university_data(user_question.strip())
            
            # Update chat history
            st.session_state["chat_history"].append({"role": "user", "content": user_question})
            st.session_state["chat_history"].append({"role": "assistant", "content": relevant_data})

            # Display the answer
            st.markdown("### 🤖 Here's what I found:")
            st.write(relevant_data)
        else:
            st.warning("⚠️ Please enter a question before asking.")

    # Display chat history
    st.markdown("### 💬 Chat History")
    for message in st.session_state["chat_history"]:
        if message["role"] == "user":
            st.markdown(f"**🧑 You:** {message['content']}")
        else:
            st.markdown(f"**🤖 Bot:** {message['content']}")

    # Clear chat history button
    if st.button("Clear Chat History ❌", key="clear_history_button"):
        st.session_state["chat_history"].clear()
        st.success("Chat history cleared.")

    # Heading about the model's purpose
    st.markdown("### 🔍 About Campus Insight AI")
    st.write(
        """
        Campus Insight AI is designed to assist students, staff, and visitors by providing instant information about COMSATS University Islamabad, Sahiwal Campus. 
        The bot uses a combination of web scraping and natural language processing to fetch and summarize relevant information from official university platforms.
        """
     )
# Footer
    st.markdown("---")
    st.markdown(
       '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
        unsafe_allow_html=True
      )

# Ensure Poppins font is applied globally
   st.markdown("""
     <style>
     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
     .stApp {
        font-family: 'Poppins', sans-serif;
     }
    </style>
   """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
