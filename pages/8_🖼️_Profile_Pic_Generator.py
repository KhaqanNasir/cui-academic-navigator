import streamlit as st
from PIL import Image, ImageDraw
import zipfile
import os
from io import BytesIO
from rembg import remove
import random
from tempfile import TemporaryDirectory

# Set up the Streamlit app with title, icon, and layout
st.set_page_config(
    page_title="Profile Picture Generator",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply Poppins font globally
st.markdown(
    """<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
    </style>""",
    unsafe_allow_html=True,
)

# Title and description
st.title("🎨 **Welcome to the Profile Picture Generator!** 🖼️")
st.write(
    """
    🌟 **Create Stunning Profile Pictures in Just a Few Clicks!** 🌟  
    📸 Upload your photo, and let our AI do the magic!  
    🎨 Generate **50+ HD-quality profile pictures** with unique, vibrant backgrounds.  
    🔽 **Download all your amazing profile pictures in a ZIP file!** 🔽  
    """
)

# Function to generate solid color backgrounds
def generate_solid_color_images(image, count=10):
    images = []
    for _ in range(count):
        color = tuple(random.choices(range(50, 256), k=3))
        bg = Image.new("RGBA", image.size, color)
        combined = Image.alpha_composite(bg, image)
        images.append(combined.convert("RGB"))
    return images

# Function to generate gradient backgrounds
def generate_gradient_images(image, count=10):
    images = []
    for _ in range(count):
        gradient = Image.new("RGBA", image.size)
        draw = ImageDraw.Draw(gradient)
        start_color = tuple(random.choices(range(50, 256), k=3))
        end_color = tuple(random.choices(range(50, 256), k=3))
        for y in range(image.size[1]):
            ratio = y / image.size[1]
            r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
            g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
            b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
            draw.line([(0, y), (image.size[0], y)], fill=(r, g, b, 255))
        combined = Image.alpha_composite(gradient.convert("RGBA"), image)
        images.append(combined.convert("RGB"))
    return images

# Upload photo
uploaded_file = st.file_uploader("📤 **Upload Your Photo** (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    try:
        with st.spinner("⏳ Processing your image... ✨"):
            # Load and process the uploaded image
            input_image = Image.open(uploaded_file).convert("RGBA")
            input_buffer = BytesIO()
            input_image.save(input_buffer, format="PNG")
            input_buffer.seek(0)

            # Remove background
            output_bytes = remove(input_buffer.getvalue())
            processed_image = Image.open(BytesIO(output_bytes)).convert("RGBA")

            # Show preview of processed image
            st.image(processed_image, caption="✅ Background Removed Successfully!", use_container_width=True)

            # Generate button
            if st.button("🚀 **Generate 50+ Profile Pictures**"):
                with st.spinner("🎨 Generating your profile pictures... 🚀"):
                    with TemporaryDirectory() as output_dir:
                        # Generate images with various backgrounds
                        solid_color_images = generate_solid_color_images(processed_image, count=10)
                        gradient_images = generate_gradient_images(processed_image, count=20)
                        rgb_images = generate_solid_color_images(processed_image, count=20)

                        # Save images to temporary directory
                        all_images = solid_color_images + gradient_images + rgb_images
                        for idx, img in enumerate(all_images):
                            img.save(os.path.join(output_dir, f"profile_{idx+1}.jpg"), "JPEG")

                        # Create ZIP file for download
                        zip_buffer = BytesIO()
                        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                            for filename in os.listdir(output_dir):
                                file_path = os.path.join(output_dir, filename)
                                zip_file.write(file_path, filename)
                        zip_buffer.seek(0)

                    # Download button for ZIP file
                    st.success("✅ **50+ Profile Pictures Generated!** 🎉")
                    st.download_button(
                        "📥 **Download All Images as ZIP**",
                        zip_buffer,
                        file_name="Profile_Pictures.zip",
                        mime="application/zip",
                    )
    except Exception as e:
        st.error(f"❌ An error occurred while processing: {e}")

# "About the Model" Section
st.subheader("📚 **About the Model**")
st.write(
    """
    - 🤖 **RemBG:** Removes the background from uploaded images with AI precision.  
    - 🖌️ **Pillow:** Applies a variety of colorful, artistic background styles to your photos.  
    - 🎛️ **Streamlit:** Creates an intuitive and user-friendly interface to bring this app to life.  
    """
)
st.write("⚡ **Fast, Fun, and Free to Use!** 🚀")

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
    unsafe_allow_html=True
)
