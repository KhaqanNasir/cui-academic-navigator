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
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
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
    st.markdown("""
     <p style='text-align:center; font-size: 22px; line-height: 1.8;'>
        🤝 Crafted with love and precision by your dedicated team! 🎨✨
        <br><br>
        Our team has put in countless hours to design and develop this platform with the goal of offering the best user experience and helping students achieve their academic goals. 
        We're always here to assist, innovate, and evolve with you! 🚀
        <br><br>
        Thank you for using the CUI Sahiwal Academic Navigator! We hope it empowers your educational journey ❤️.
     </p>
    """, unsafe_allow_html=True)

    
    st.markdown("<h2 style='text-align:center;'>👨‍💻 Meet the Team 🚀</h2>", unsafe_allow_html=True)
    
    # Team members
    team_members = [
        {
            "name": "💻 Muhammad Khaqan Nasir",
            "registration_no": "FA22-BCS-039",
            "github": "KhaqanNasir",
            "linkedin": "khaqan-nasir",
        "image": os.path.join(os.path.dirname(__file__), 'assets', 'Profile_Pic_Updat.jpg') 
        }
        # },
        # {
        #     "name": "🖥️ Khadija Riaz",
        #     "registration_no": "FA22-BCS-038",
        #     "github": "#",
        #     "linkedin": "#",
        #     "image": os.path.join(os.path.dirname(__file__), 'assets', 'Profile_Pic_Updat.jpg')  
        # },
        # {
        #     "name": "🖥️ Ahsan Abdullah",
        #     "registration_no": "FA22-BCS-015",
        #     "github": "#",
        #     "linkedin": "#",
        #     "image": os.path.join(os.path.dirname(__file__), 'assets', 'member01.jpeg')  
        # }
    ]
    
    # Display team members
    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        with col:
            # Encode image to base64
            encoded_image = encode_image(member['image'])
        
            # HTML structure with background color and adjusted image height
            st.markdown(f"""
            <div style='background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center;'>
                <div style='background-color: #ffffff; border-radius: 50%; width: 200px; height: 200px; margin: 0 auto; display: flex; justify-content: center; align-items: center;'>
                    <img src="data:image/jpeg;base64,{encoded_image}" alt="{member['name']}" style='width: 100%; height: 100%; object-fit: cover; border-radius: 50%;'>
                </div>
                <div style='font-size: 22px; font-weight: 600; color: #5F6366; margin-top: 10px;'>{member['name']}</div>
                <div style='font-size: 18px; color: #5F6366;'>{member['registration_no']}</div>
                <div style='font-size: 18px; color: #5F6366; margin-top: 5px;'>
                    <a href='https://github.com/{member["github"]}' target='_blank' style='font-size: 20px; color: #000000; margin-right: 10px;'>
                        <i class="fab fa-github" style="font-size: 20px; color: #000000; margin-right: 5px;"></i> GitHub
                    </a>
                    <a href='https://linkedin.com/in/{member["linkedin"]}' target='_blank' style='font-size: 20px; color: #0077B5;'>
                        <i class="fab fa-linkedin" style="font-size: 20px; color: #0077B5; margin-right: 5px;"></i> LinkedIn
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
       unsafe_allow_html=True)       

if __name__ == "__main__":
    st.set_page_config(
        page_title="About Us - CUI Sahiwal Academic Navigator",
        page_icon="🎓",
        layout="wide",  # Wide layout for better presentation
        initial_sidebar_state="collapsed"
    )
    main()
