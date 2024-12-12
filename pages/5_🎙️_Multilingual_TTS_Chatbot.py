# import streamlit as st
# from gtts import gTTS
# from pydub import AudioSegment
# import io

# # Set Streamlit layout to wide
# st.set_page_config(layout="wide", page_title="Multilingual TTS Chatbot", page_icon="🎙️")

# # Apply Google Fonts (Poppins)
# st.markdown(
#     """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
#     body {
#         font-family: 'Poppins', sans-serif;
#     }
#     .stButton > button {
#         background-color: #4CAF50;
#         color: white;
#         font-size: 16px;
#         font-weight: bold;
#         border-radius: 12px;
#         padding: 12px 24px;
#         margin-top: 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True
# )

# # Extended language options for gTTS
# LANGUAGES = {
#     "English": "en",
#     "French": "fr",
#     "German": "de",
#     "Spanish": "es",
#     "Italian": "it",
#     "Russian": "ru",
#     "Hindi": "hi",
#     "Arabic": "ar",
#     "Portuguese": "pt",
#     "Dutch": "nl",
#     "Urdu": "ur",
#     "Punjabi": "pa",
#     "Bengali": "bn",
#     "Tamil": "ta",
#     "Telugu": "te",
#     "Gujarati": "gu",
#     "Malayalam": "ml",
#     "Marathi": "mr",
#     "Japanese": "ja",
#     "Chinese (Mandarin)": "zh"
# }

# # Main UI
# st.title("🎙️ Multilingual Text-to-Speech Chatbot")
# st.subheader("Generate speech in your preferred language, voice, and tone.")

# # Language selection
# language = st.selectbox("🌍 Select Language", options=list(LANGUAGES.keys()))

# # Voice selection (Gender is not directly supported by gTTS)
# gender = st.radio("🎭 Select Voice", options=["Male", "Female"])

# # Pitch and tone adjustments (Simulate via pydub)
# st.markdown("🎚️ **Pitch and Tone Adjustments**")
# pitch = st.slider("Pitch", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
# tone = st.slider("Tone", min_value=0.5, max_value=2.0, value=1.0, step=0.1)

# # Text input
# text = st.text_area("📝 Enter Text to Generate Speech", "")

# # Generate Button
# if st.button("Generate Voice"):
#     if not text.strip():
#         st.warning("⚠️ Please enter some text to synthesize!")
#     else:
#         try:
#             # Use gTTS to generate speech
#             tts = gTTS(text=text, lang=LANGUAGES[language], slow=False)

#             # Save the generated speech to a BytesIO buffer
#             mp3_buffer = io.BytesIO()
#             tts.write_to_fp(mp3_buffer)
#             mp3_buffer.seek(0)

#             # Apply pitch and tone manipulation using pydub
#             sound = AudioSegment.from_file(mp3_buffer, format="mp3")
#             new_speed = pitch  # Adjust the speed for pitch control
#             sound = sound.speedup(playback_speed=new_speed)

#             # Save modified audio to a new BytesIO buffer
#             modified_buffer = io.BytesIO()
#             sound.export(modified_buffer, format="mp3")
#             modified_buffer.seek(0)

#             # Provide the audio in Streamlit
#             st.audio(modified_buffer, format="audio/mp3")
#             st.success("✅ Voice generated successfully!")

#             # Provide download button for the generated speech
#             st.download_button(
#                 label="⬇️ Download MP3",
#                 data=modified_buffer,
#                 file_name="generated_voice.mp3",
#                 mime="audio/mp3",
#             )

#         except Exception as e:
#             st.error(f"❌ An error occurred: {str(e)}")

# # Footer
# st.markdown("💻 **Powered by gTTS** | Free resources for TTS generation.")
# st.markdown("---")
# st.markdown(
#     '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
#     unsafe_allow_html=True
# )

# import os
# import streamlit as st
# from gtts import gTTS
# from pydub import AudioSegment
# import io

# # Set Streamlit layout to wide
# st.set_page_config(layout="wide", page_title="Multilingual TTS Chatbot", page_icon="🎙️")

# # Apply Google Fonts (Poppins)
# st.markdown(
#     """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
#     body {
#         font-family: 'Poppins', sans-serif;
#     }
#     .stButton > button {
#         background-color: #4CAF50;
#         color: white;
#         font-size: 16px;
#         font-weight: bold;
#         border-radius: 12px;
#         padding: 12px 24px;
#         margin-top: 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True
# )

# # Ensure ffmpeg is set (update path if necessary)
# AudioSegment.converter = "ffmpeg"  # Replace with the absolute path to ffmpeg if needed

# # Extended language options for gTTS
# LANGUAGES = {
#     "English": "en",
#     "French": "fr",
#     "German": "de",
#     "Spanish": "es",
#     "Italian": "it",
#     "Russian": "ru",
#     "Hindi": "hi",
#     "Arabic": "ar",
#     "Portuguese": "pt",
#     "Dutch": "nl",
#     "Urdu": "ur",
#     "Punjabi": "pa",
#     "Bengali": "bn",
#     "Tamil": "ta",
#     "Telugu": "te",
#     "Gujarati": "gu",
#     "Malayalam": "ml",
#     "Marathi": "mr",
#     "Japanese": "ja",
#     "Chinese (Mandarin)": "zh"
# }

# # Main UI
# st.title("🎙️ Multilingual Text-to-Speech Chatbot")
# st.subheader("Generate speech in your preferred language, voice, and tone.")

# # Language selection
# language = st.selectbox("🌍 Select Language", options=list(LANGUAGES.keys()))

# # Voice selection (Gender simulation using speed adjustment)
# gender = st.radio("🎭 Select Voice", options=["Male", "Female"])

# # Pitch and tone adjustments (Simulated via pydub)
# st.markdown("🎚️ **Pitch and Tone Adjustments**")
# pitch = st.slider("Pitch", min_value=0.5, max_value=2.0, value=1.0, step=0.1)

# # Text input
# text = st.text_area("📝 Enter Text to Generate Speech", "")

# # Generate Button
# if st.button("Generate Voice"):
#     if not text.strip():
#         st.warning("⚠️ Please enter some text to synthesize!")
#     else:
#         try:
#             # Use gTTS to generate speech
#             tts = gTTS(
#                 text=text, 
#                 lang=LANGUAGES[language], 
#                 slow=(gender == "Male")
#             )

#             # Save the generated speech to a BytesIO buffer
#             mp3_buffer = io.BytesIO()
#             tts.write_to_fp(mp3_buffer)
#             mp3_buffer.seek(0)

#             # Load the audio for manipulation
#             sound = AudioSegment.from_file(mp3_buffer, format="mp3")

#             # Apply pitch adjustment using playback speed
#             adjusted_speed = pitch
#             sound = sound.speedup(playback_speed=adjusted_speed, crossfade=0)

#             # Save the modified audio to a new buffer
#             modified_buffer = io.BytesIO()
#             sound.export(modified_buffer, format="mp3")
#             modified_buffer.seek(0)

#             # Provide the audio in Streamlit
#             st.audio(modified_buffer, format="audio/mp3")
#             st.success("✅ Voice generated successfully!")

#             # Provide download button for the generated speech
#             st.download_button(
#                 label="⬇️ Download MP3",
#                 data=modified_buffer,
#                 file_name="generated_voice.mp3",
#                 mime="audio/mp3",
#             )

#         except FileNotFoundError as e:
#             st.error(
#                 "❌ `ffmpeg` not found. Please ensure it's installed and added to your system PATH."
#             )
#         except Exception as e:
#             st.error(f"❌ An error occurred: {str(e)}")

# # Footer
# st.markdown("---")
# st.markdown(
#     '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
#     unsafe_allow_html=True
# )

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
st.subheader("Generate speech in your preferred language, voice, and tone.")

# Language selection
language = st.selectbox("🌍 Select Language", options=list(LANGUAGES.keys()))

# Voice selection (Gender is not directly supported by gTTS)
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

            # Save the generated speech to a BytesIO buffer
            mp3_buffer = io.BytesIO()
            tts.write_to_fp(mp3_buffer)
            mp3_buffer.seek(0)

            # Apply pitch and tone manipulation using pydub
            sound = AudioSegment.from_file(mp3_buffer, format="mp3")
            
            # Apply pitch adjustment by changing the speed
            sound = sound.speedup(playback_speed=pitch)
            
            # If you want to simulate tone adjustments, you can modify the volume or apply other effects
            sound = sound + (tone - 1) * 10  # Adjust volume based on tone (this is an approximation)

            # Save modified audio to a new BytesIO buffer
            modified_buffer = io.BytesIO()
            sound.export(modified_buffer, format="mp3")
            modified_buffer.seek(0)

            # Provide the audio in Streamlit
            st.audio(modified_buffer, format="audio/mp3")
            st.success("✅ Voice generated successfully!")

            # Provide download button for the generated speech
            st.download_button(
                label="⬇️ Download MP3",
                data=modified_buffer,
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
