import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
import os
import io

# Set Streamlit layout to wide
st.set_page_config(layout="wide", page_title="Multilingual TTS Chatbot", page_icon="🎙️")

# Apply Google Fonts (Poppins)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    body {
        font-family: 'Poppins', sans-serif;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Extended language options for gTTS
LANGUAGES = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Russian": "ru",
    "Hindi": "hi",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Urdu": "ur",           
    "Punjabi": "pa",        
    "Bengali": "bn",         
    "Tamil": "ta",           
    "Telugu": "te",         
    "Gujarati": "gu",        
    "Malayalam": "ml",       
    "Marathi": "mr",         
    "Japanese": "ja",        
    "Chinese (Mandarin)": "zh" #
}

# Main UI
st.title("🎙️ Multilingual Text-to-Speech Chatbot")
st.subheader("Generate speech in your preferred language, voice, and tone.")

# Language selection
language = st.selectbox("🌍 Select Language", options=list(LANGUAGES.keys()))

# Voice selection (Gender is not directly supported by gTTS, so we work around this by allowing different languages with different voices)
gender = st.radio("🎭 Select Voice", options=["Male", "Female"])

# Pitch and tone adjustments (Simulate via pydub)
st.markdown("🎚️ **Pitch and Tone Adjustments**")
pitch = st.slider("Pitch", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
tone = st.slider("Tone", min_value=0.5, max_value=2.0, value=1.0, step=0.1)

# Text input
text = st.text_area("📝 Enter Text to Generate Speech", "")

# Generate Button
if st.button("Generate Voice"):
    if not text.strip():
        st.warning("⚠️ Please enter some text to synthesize!")
    else:
        try:
            # Use gTTS to generate speech
            tts = gTTS(text=text, lang=LANGUAGES[language], slow=False)

            # Save the generated speech to an in-memory file
            speech_file = "/content/generated_voice.mp3"
            tts.save(speech_file)

            # Apply pitch and tone manipulation using pydub
            sound = AudioSegment.from_mp3(speech_file)

            # Change pitch by altering the speed of the audio (faster = higher pitch, slower = lower pitch)
            new_speed = pitch  # Adjust the speed for pitch control
            sound = sound.speedup(playback_speed=new_speed)

            # Change tone (volume or pitch range manipulation)
            tone_factor = tone  # Adjust volume or pitch range
            sound = sound + (tone_factor - 1.0) * 10  # Adjust volume by scaling

            # Save the modified audio file
            modified_file = "generated_voice.mp3"
            sound.export(modified_file, format="mp3")

            # Provide the audio in Streamlit
            st.audio(modified_file, format="audio/mp3")
            st.success("✅ Voice generated successfully!")

            # Provide download button for the generated speech
            with open(modified_file, "rb") as file:
                st.download_button(
                    label="⬇️ Download MP3",
                    data=file,
                    file_name="generated_voice.mp3",
                    mime="audio/mp3",
                )

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("💻 **Powered by gTTS** | Free resources for TTS generation.")
