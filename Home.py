import streamlit as st
import base64

# === THEME TOGGLE ===
theme = st.sidebar.radio("Choose Theme", ("Light Mode", "Dark Mode"))

# Inject Theme CSS
if theme == "Dark Mode":
    st.markdown("""
        <style>
        html, body, [class*="css"] {
            background-color: #111 !important;
            color: #f5f5f5 !important;
        }
        .nav-button, .feature-card {
            background-color: #222 !important;
            color: #f5f5f5 !important;
            border-color: #444 !important;
        }
        .feature-card:hover {
            background-color: #444 !important;
            color: #fff !important;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        html, body, [class*="css"] {
            background-color: #f9fafa !important;
            color: #000 !important;
        }
        </style>
    """, unsafe_allow_html=True)

# === Load and Encode Logo ===
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load logo as base64
logo_base64 = get_base64_image("logo.jpeg")

# === STYLING ===
st.markdown(f"""<style> ... </style>""", unsafe_allow_html=True)
# (your full style block and HTML remains here unchanged)
