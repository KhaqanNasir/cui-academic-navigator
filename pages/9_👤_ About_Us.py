import streamlit as st
import os
import base64

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .stApp {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

def encode_image(image_path):
    # Read and encode image in base64 format
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_image

def main():
    load_css()
    
    # Main Title
    st.markdown("<h1 style='text-align:center;'>🌟 About Us 🌟</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>🤝 Crafted with love and precision by your dedicated team! 🎨✨</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center;'>👨‍💻 Meet the Team 🚀</h2>", unsafe_allow_html=True)
    
    # Team members
    team_members = [
        {
            "name": "💻 Muhammad Khaqan Nasir",
            "registration_no": "FA22-BCS-039",
            "github": "#",
            "linkedin": "#",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'Profile_Pic_Updat.jpg')  # Path to local image
        },
        {
            "name": "🖥️ Khadija Riaz",
            "registration_no": "FA22-BCS-038",
            "github": "#",
            "linkedin": "#",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member2.jpg')  # Path to local image
        },
        {
            "name": "🖥️ Ahsan Abdullah",
            "registration_no": "FA22-BCS-015",
            "github": "#",
            "linkedin": "#",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member3.jpg')  # Path to local image
        }
    ]
    
    # Display team members
    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        with col:
            # Encode image to base64
            encoded_image = encode_image(member['image'])
            st.markdown(f"""
                <div style='background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center;'>
                    <div style='border-radius: 50%; overflow: hidden; width: 150px; height: 150px; margin: 0 auto;'>
                        <img src="data:image/jpeg;base64,{encoded_image}" alt="{member['name']}" style='width:100%; height:100%; object-fit: cover;'>
                    </div>
                    <div style='font-size: 22px; font-weight: 600; color: #5F6366;'>{member['name']}</div>
                    <div style='font-size: 18px; color: #5F6366;'>{member['registration_no']}</div>
                    <div style='margin-top: 10px;'>
                        <a href='https://github.com/{member["github"]}' target='_blank' style='text-decoration: none; font-size: 14px;'>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" style="fill:#000000;">
                                <path d="M12 2C6.48 2 2 6.48 2 12c0 4.99 3.67 9.17 8.5 10.64v-7.55h-2.56v-2.62h2.56v-2c0-2.53 1.5-3.93 3.84-3.93 1.11 0 2.28.08 2.58.12v2.85h-1.73c-1.35 0-1.79.84-1.79 1.69v2.16h3.04l-.49 2.62h-2.55v7.58c4.83-.83 8.5-4.9 8.5-9.64 0-5.52-4.48-10-10-10z"/>
                            </svg>
                            GitHub
                        </a>
                        <a href='https://linkedin.com/in/{member["linkedin"]}' target='_blank' style='text-decoration: none; font-size: 14px; color: #007bff; margin-left: 10px;'>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" style="fill:#007bff;">
                                <path d="M19 0H5C3.9 0 3 .9 3 2v20c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V2c0-1.1-.9-2-2-2zM8.5 17h-2v-7h2v7zM7.5 9.75c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM18 17h-2v-3.5c0-1.12-.91-2-2-2s-2 .88-2 2V17h-2v-7h2v1.09c.34-.62 1.04-1.09 1.89-1.09 1.48 0 2.61 1.25 2.61 2.61V17z"/>
                            </svg>
                            LinkedIn
                        </a>
                    </div>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(
        page_title="About Us - CUI Sahiwal Academic Navigator",
        page_icon="🎓",
        layout="wide",  # Wide layout for better presentation
        initial_sidebar_state="collapsed"
    )
    main()
