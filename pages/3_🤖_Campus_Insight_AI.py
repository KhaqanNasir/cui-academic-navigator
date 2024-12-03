import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up the Selenium WebDriver with options
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service(executable_path="/path/to/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Function to fetch data from websites with Selenium
def fetch_university_data_selenium(query):
    urls = [website_url, facebook_url, instagram_url, linkedin_url]
    relevant_info = ""
    
    for url in urls:
        driver = setup_driver()
        driver.get(url)
        time.sleep(5)  # Wait for the page to load completely
        
        # Example for extracting content from paragraphs or specific sections
        try:
            content = driver.find_elements(By.TAG_NAME, "p")  # Extract all <p> tags
            for element in content:
                if query.lower() in element.text.lower():
                    relevant_info += f"🔗 **From {url}**: {element.text}\n"
        except Exception as e:
            relevant_info += f"❌ Error fetching data from {url}: {e}\n"
        finally:
            driver.quit()  # Close the browser after scraping

    return relevant_info if relevant_info else "⚠️ Sorry, I couldn't find relevant information on the websites."

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
            # Fetch relevant data using Selenium
            relevant_data = fetch_university_data_selenium(user_question.strip())
            
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
    st.markdown(
      '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
       unsafe_allow_html=True)

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
