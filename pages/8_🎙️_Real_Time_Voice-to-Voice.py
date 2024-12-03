import os
import streamlit as st
from gtts import gTTS
import io
from transformers import pipeline

# Set up a Hugging Face Transformers pipeline for text generation as a substitute for Groq
text_generation = pipeline("text-generation", model="gpt2")  # Lightweight alternative

def process_text(text):
    try:
        # Generate LLM response using Hugging Face pipeline
        response_message = text_generation(text, max_length=100, do_sample=True)[0]["generated_text"]

        # Convert text response to speech using gTTS
        tts = gTTS(response_message)
        response_audio_io = io.BytesIO()
        tts.write_to_fp(response_audio_io)  # Save the audio to the BytesIO object
        response_audio_io.seek(0)

        # Save the response audio file
        with open("response.mp3", "wb") as audio_file:
            audio_file.write(response_audio_io.getvalue())

        return response_message, "response.mp3"

    except Exception as e:
        return f"An error occurred: {e}", None

# Streamlit UI setup
st.set_page_config(page_title="Text-to-Voice Chatbot", page_icon="🎙️", layout="wide")

# Load Poppins font from Google Fonts
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        body {
            font-family: 'Poppins', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Main title with icons
st.title("🎙️ Real-Time Text-to-Voice Chatbot 🚀")
st.markdown("Developed by [Muhammad Khaqan Nasir](https://www.linkedin.com/in/khaqan-nasir/) 🤝", unsafe_allow_html=True)

# Instructions with additional engaging icons
st.markdown("""
    ### 📋 Instructions:
    1. 📝 **Enter** text into the input box.
    2. 🔘 **Click** the Generate button to process and generate a response.
    3. 🎧 **Listen** to the chatbot's response.
    4. 🌟 **Enjoy** the interactive conversation with the bot!
""")

# Text input for user query
user_input = st.text_area("✍️ Type your question or message here:")

# Generate button
if st.button("Generate"):
    if user_input.strip():
        # Process the text input
        response_text, response_audio_path = process_text(user_input)

        # Display the response text
        st.subheader("💬 Response Text:")
        st.write(response_text)

        # Play the audio response
        if response_audio_path:
            audio_file = open(response_audio_path, 'rb')
            st.audio(audio_file.read(), format="audio/mp3")
    else:
        st.warning("Please enter some text before clicking Generate!")

# About section with more icons for engagement
st.markdown("""
    ## 📖 About the Bot
    This real-time text-to-voice chatbot utilizes the power of **GPT-2** for text generation. The chatbot processes your text input, generates a response, and converts it back to speech, providing a seamless and engaging user experience. 

    ### 🧠 Model Used:
    - **GPT-2**: Generates the chatbot's responses in text form.
    - **gTTS**: Converts the generated text back to speech.

    ### 🤖 Use Case:
    This bot is designed to provide interactive conversations, where users type their message, hear the transcription, and get voice responses from the bot in real time.
""")

# Add additional section for enhancement and call to action
st.markdown("""
    ## 🚀 Try It Now!
    🔥 Engage with the real-time text-to-voice chatbot. Type your message, click Generate, and hear back your personalized response! It's quick, fun, and intelligent. 
    - 📝 **Type** your message to the bot
    - 🎧 **Hear** back the responses
    - 🤖 **Experience** real-time AI-powered conversation!

    ### 🌟 Get Started:
    Simply type your message and click Generate to start the conversation.
""")

# Footer
st.markdown(
    '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
    unsafe_allow_html=True
)
