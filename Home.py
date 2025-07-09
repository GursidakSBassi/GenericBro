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
    color: #02899d;
    margin-top: 3rem;
    margin-bottom: 1rem;
    font-weight: 600;
}}
</style>
""", unsafe_allow_html=True)

# === Top Section ===
st.markdown(f"""
<div class="container">
    <img src="data:image/jpeg;base64,{logo_base64}" class="logo" />
    <h1 class="main-title">GenericBro</h1>
    <p class="subtitle">💊 Compare medicines, find pharmacies & digitize prescriptions.</p>
</div>
<div class="moving-text-container">
    <div class="moving-text">Welcome to GenericBro - Empowering Affordable Healthcare with AI ⚕️</div>
</div>
""", unsafe_allow_html=True)

# === Navigation Section (New) ===
st.markdown('<h3 class="features-title">🛠️ Explore Our Tools</h3>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Generic Medicine Finder.py", label="🔍 Generic Medicine Finder")

with col2:
    st.page_link("pages/Pharmacy Locator.py", label="📍 Pharmacy Locator")

with col3:
    st.page_link("pages/Prescription Reader.py", label="📄 Prescription Reader")

# === Keep your future contents here ===
st.markdown("---")
st.markdown("✅ More features and insights coming soon. Stay tuned!")
