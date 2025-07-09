import streamlit as st
import base64

# === Load and Encode Logo ===
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load logo as base64
logo_base64 = get_base64_image("logo.jpeg")

# === STYLING ===
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    background-color: #f9fafa;
}}

.moving-text-container {{
    overflow: hidden;
    white-space: nowrap;
    background: linear-gradient(90deg, #02899d, #4db6ac);
    color: white;
    padding: 12px 0;
    margin-bottom: 2rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}}

.moving-text {{
    display: inline-block;
    animation: scroll-left 25s linear infinite;
    font-size: 1.1rem;
    font-weight: 500;
    padding-left: 100%;
}}

@keyframes scroll-left {{
    0% {{ transform: translateX(0); }}
    100% {{ transform: translateX(-100%); }}
}}

.container {{
    max-width: 900px;
    margin: auto;
    padding: 3rem 2rem;
    text-align: center;
}}

.logo {{
    width: 160px;
    margin-bottom: 1rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
    border-radius: 12px;
}}

.main-title {{
    font-size: 2.5rem;
    font-weight: 700;
    color: #02899d;
    margin: 0.5rem 0;
}}

.subtitle {{
    font-size: 1.1rem;
    color: #444;
    margin-bottom: 2.5rem;
}}

.features-title {{
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 2rem;
    margin-bottom: 1.5rem;
    color: #222;
}}

.feature-card {{
    background-color: #ffffff;
    border: 2px solid #02899d;
    color: #02899d;
    padding: 1.2rem 1rem;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 12px;
    transition: all 0.3s ease;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}}

.feature-card:hover {{
    background-color: #02899d;
    color: white;
    transform: scale(1.03);
}}
</style>
""", unsafe_allow_html=True)

# === Redirect Buttons ===
st.markdown("## 🔗 Jump to Tools")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Generic Medicine Finder.py", label="🔍 Generic Medicine Finder")

with col2:
    st.page_link("pages/Pharmacy Locator.py", label="📍 Pharmacy Locator")

with col3:
    st.page_link("pages/Prescription Reader.py", label="📄 Prescription Reader")
