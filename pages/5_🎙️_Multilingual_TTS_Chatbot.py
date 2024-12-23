import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
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
    "Chinese (Mandarin)": "zh"
}

# Main UI
st.title("🎙️ Multilingual Text-to-Speech Chatbot")
st.subheader("Generate speech in your preferred language.")

# Language selection
language = st.selectbox("🌍 Select Language", options=list(LANGUAGES.keys()))

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

            # Save the generated speech to a BytesIO buffer
            mp3_buffer = io.BytesIO()
            tts.write_to_fp(mp3_buffer)
            mp3_buffer.seek(0)

            # Load audio using pydub (ensure it's processed correctly)
            sound = AudioSegment.from_file(mp3_buffer, format="mp3")
            
            # Provide the audio in Streamlit
            st.audio(mp3_buffer, format="audio/mp3")
            st.success("✅ Voice generated successfully!")

            # Provide download button for the generated speech
            st.download_button(
                label="⬇️ Download MP3",
                data=mp3_buffer,
                file_name="generated_voice.mp3",
                mime="audio/mp3",
            )

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("💻 **Powered by gTTS** | Free resources for TTS generation.")
st.markdown("---")
st.markdown(
    '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
    unsafe_allow_html=True
)
