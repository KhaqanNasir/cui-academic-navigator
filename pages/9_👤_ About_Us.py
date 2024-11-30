import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .stApp {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

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
            "image": "#"  # Replace with your image URL
        },
        {
            "name": "🖥️ Khadija Riaz",
            "registration_no": "FA22-BCS-038",
            "github": "#",
            "linkedin": "#",
            "image": "#"  # Replace with your friend's image URL
        },
        {
            "name": "🖥️ Ahsan Abdullah",
            "registration_no": "FA22-BCS-015",
            "github": "#",
            "linkedin": "#",
            "image": "#"  # Replace with your friend's image URL
        }
    ]
    
    # Display team members
    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        with col:
            st.markdown(f"""
                <div style='background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center;'>
                    <div style='border-radius: 50%; overflow: hidden; width: 150px; height: 150px; margin: 0 auto;'>
                        <img src="{member['image']}" alt="{member['name']}" style='width:100%; height:100%; object-fit: cover;'>
                    </div>
                    <div style='font-size: 22px; font-weight: 600; color: #5F6366;'>{member['name']}</div>
                    <div style='font-size: 18px; color: #5F6366;'>{member['registration_no']}</div>
                    <div style='margin-top: 10px;'>
                        <a href='https://github.com/{member["github"]}' target='_blank' style='text-decoration: none; font-size: 14px; color: #007bff;'>🐙 GitHub</a>
                        <a href='https://linkedin.com/in/{member["linkedin"]}' target='_blank' style='text-decoration: none; font-size: 14px; color: #007bff; margin-left: 10px;'>🔗 LinkedIn</a>
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
