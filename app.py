# app.py
import streamlit as st
import os
from api_utils import analyze_image_with_llava
from PIL import Image

# Ensure the images folder exists
if not os.path.exists("images"):
    os.makedirs("images")

st.set_page_config(page_title="GIS Image Analyzer", layout="wide")
st.title("🌍 GIS Satellite Image Analyzer with LLaVA)")

# Upload Form
st.markdown("Upload a satellite image to analyze land use and features.")

uploaded_file = st.file_uploader("🛰️ Upload Image (jpg, png)", type=["jpg", "jpeg", "png"])
location_name = st.text_input("📍 Location Name (Optional)")

if uploaded_file and st.button("Analyze Image"):
    file_path = os.path.join("images", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.image(Image.open(file_path), caption="Uploaded Image", use_column_width=True)
    st.info("⏳ Analyzing image using LLaVA...")

    result = analyze_image_with_llava(file_path)
    st.success("✅ Analysis Complete!")
    st.markdown(f"**🧠 AI Analysis Result:**\n\n{result}")
