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

.get-started {{
    text-align: left;
    margin-top: 2.5rem;
}}

.get-started h3 {{
    font-size: 1.3rem;
    color: #02899d;
}}

.get-started ul {{
    font-size: 1rem;
    color: #444;
    margin-top: 0.5rem;
}}

.footer {{
    margin-top: 3rem;
    font-size: 0.9rem;
    color: #999;
    text-align: center;
}}
</style>

<!-- Moving text banner -->
<div class="moving-text-container">
    <div class="moving-text">
        💊 Find Generic Medicines at Affordable Prices | 📍 Locate Nearby Pharmacies | 📝 Upload Prescriptions for Easy Medicine Extraction | 🏥 Your Health, Our Priority | 💰 Save Money on Healthcare | 🌟 Trusted by Thousands
    </div>
</div>

<div class="container">
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{logo_base64}" class="logo" />
        <div class="main-title">GenericBro</div>
        <div class="subtitle">
            Affordable Healthcare at Your Fingertips.<br>
            Find <b>generic alternatives</b> and <b>locate pharmacies</b> instantly.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# === FEATURE CARDS (non-clickable) ===
st.markdown('<div class="features-title">🔍 What can you do with GenericBro?</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-card">💊 Generic Medicine Finder</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-card">📍 Pharmacy Locator</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature-card">📝 Prescription Reader</div>', unsafe_allow_html=True)

# === GET STARTED ===
st.markdown("""
<div class="get-started">
    <h3>🚀 Get Started</h3>
    <ul>
        <li><b>Generic Medicine Finder</b>: Discover affordable alternatives.</li>
        <li><b>Pharmacy Locator</b>: Find nearby pharmacies with ease.</li>
        <li><b>Prescription Reader</b>: Upload prescriptions to extract medicine names.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# === FOOTER ===
st.markdown("""
<div class="footer">
    Built with ❤️ by Team GenericBro. <br>
    <div style="margin-top: 1rem; display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 15px;">
        <span style="background: linear-gradient(135deg, #02899d, #4db6ac); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">👨‍💻 Nidhish</span>
        <span style="background: linear-gradient(135deg, #ff6b6b, #ff8e8e); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">💻 Gursidak</span>
        <span style="background: linear-gradient(135deg, #a8e6cf, #7fcdcd); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">👩‍💻 Varshini</span>
        <span style="background: linear-gradient(135deg, #ffd93d, #ffb347); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">🧑‍💻 Oindrila</span>
        <span style="background: linear-gradient(135deg, #c7a8ff, #b18cff); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">💻 Atharva</span>
        <span style="background: linear-gradient(135deg, #ff9a9e, #fecfef); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">👩‍💻 Poorvi</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Close container div
st.markdown('</div>', unsafe_allow_html=True)
