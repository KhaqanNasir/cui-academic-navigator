import os
import streamlit as st
from gtts import gTTS
import io
import openai

# Access the OpenAI API key securely from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Maintain conversation history
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

# Function to generate text response using GPT-3.5
def generate_response(user_input, history, response_length):
    try:
        # Set max tokens based on response length
        max_tokens_map = {"short": 50, "medium": 100, "detailed": 200}
        max_tokens = max_tokens_map.get(response_length, 100)

        # Generate response with context from conversation history
        messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
        messages += history
        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-2",
            messages=messages,
            max_tokens=max_tokens,
        )
        response_text = response['choices'][0]['message']['content']
        return response_text, len(response_text.split())
    except Exception as e:
        return f"Error: {e}", 0

# Function to convert text to speech
def text_to_speech(response_message, language="en", pitch=1.0, speed=1.0):
    try:
        tts = gTTS(response_message, lang=language)
        response_audio_io = io.BytesIO()
        tts.write_to_fp(response_audio_io)  # Save audio to BytesIO
        response_audio_io.seek(0)

        # Save the audio response
        with open("response.mp3", "wb") as audio_file:
            audio_file.write(response_audio_io.getvalue())
        return "response.mp3"
    except Exception as e:
        return None

# Streamlit UI setup
st.set_page_config(page_title="Enhanced Text-to-Voice Chatbot", page_icon="🎙️", layout="wide")

# Load Poppins font from Google Fonts
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        body {
            font-family: 'Poppins', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Main title
st.title("🎙️ Enhanced Text-to-Voice Chatbot 🚀")

# Instructions
st.markdown("""
    ### 📋 Instructions:
    1. Type your message in the input box below.
    2. Select your response preferences (length, voice language, etc.).
    3. Click on **Generate** to get a response.
    4. Listen to the response and enjoy the interaction!
""")

# Input for user query
user_input = st.text_area("✍️ Type your question or message here:", height=150)

# Response customization
col1, col2, col3 = st.columns(3)
with col1:
    response_length = st.selectbox("🔧 Response Length:", ["short", "medium", "detailed"], index=1)
with col2:
    tts_language = st.selectbox("🌐 Language (TTS):", ["en", "es", "fr", "de", "it"])
with col3:
    tts_speed = st.slider("🎛️ Voice Speed:", 0.5, 2.0, 1.0, 0.1)

# Generate button
if st.button("Generate"):
    if user_input.strip():
        with st.spinner("Processing... Please wait."):
            # Generate response
            response_text, word_count = generate_response(user_input, st.session_state["conversation_history"], response_length)
            
            # Add user and assistant messages to conversation history
            st.session_state["conversation_history"].append({"role": "user", "content": user_input})
            st.session_state["conversation_history"].append({"role": "assistant", "content": response_text})

            # Display the response
            st.subheader("💬 Response:")
            st.write(response_text)

            # Show word count
            st.markdown(f"**📝 Word Count:** {word_count}")

            # Convert response to speech
            response_audio_path = text_to_speech(response_text, language=tts_language, speed=tts_speed)

            # Play the audio response
            if response_audio_path:
                st.audio(response_audio_path, format="audio/mp3")
            else:
                st.error("⚠️ Unable to generate audio. Please try again.")
    else:
        st.error("⚠️ Please enter a message before clicking 'Generate'.")

# About section
st.markdown("""
    ## 📖 About the Bot
    This chatbot utilizes **GPT-3.5** for generating high-quality, context-aware responses and converts them to speech using **gTTS**. It supports multi-turn conversations, customizable responses, and multiple language options for text-to-speech output.

    ### 🌟 Features:
    - Multi-turn conversation support.
    - Customizable response length (short, medium, detailed).
    - Multiple TTS languages (English, Spanish, French, etc.).
    - Adjustable voice speed for more natural playback.
""")

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
    unsafe_allow_html=True
)
