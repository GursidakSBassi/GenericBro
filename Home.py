import streamlit as st
from PIL import Image
import base64

# === Logo and Styling ===
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image("logo.jpeg")

st.set_page_config(page_title="GenericBro - Main", layout="wide")

st.markdown(f"""
    <div style="text-align:center;">
        <img src="data:image/jpeg;base64,{logo_base64}" alt="Logo" width="140" style="border-radius:16px; box-shadow:0 4px 12px rgba(0,0,0,0.15);" />
        <h1 style="color:#02899d; margin-top: 1rem;">💊 GenericBro – Your Affordable Health Companion</h1>
        <p style="font-size:1.1rem; color:#444;">Explore medicine savings, find pharmacies, and read prescriptions easily.</p>
    </div>
""", unsafe_allow_html=True)

# === Navigation to Pages ===
st.markdown("## 📂 Navigate to Tools")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Generic Medicine Finder.py", label="🔍 Generic Medicine Finder", icon="💊")

with col2:
    st.page_link("pages/Pharmacy Locator.py", label="📍 Pharmacy Locator", icon="🗺️")

with col3:
    st.page_link("pages/Prescription Reader.py", label="📝 Prescription Reader", icon="📄")

# Optional footer or info
st.markdown("""
<hr>
<p style="text-align:center; font-size:0.9rem; color:#888;">
Made with ❤️ to reduce your medical expenses.
</p>
""", unsafe_allow_html=True)
