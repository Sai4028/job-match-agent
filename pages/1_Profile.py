import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("."))

from service.resume_parser import extract_resume_text
from service.profile_manager import save_profile, load_profile
from service.profile_extractor import extract_profile


st.title("Profile Setup")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

roles = st.text_area(
    "Preferred Roles",
    placeholder="Product Manager, Senior Product Manager"
)

locations = st.text_area(
    "Preferred Locations",
    placeholder="Bengaluru, Remote"
)

if resume:

    resume_text = extract_resume_text(resume)

    api_key = st.secrets["GEMINI_API_KEY"]

    st.write("Gemini API Key Loaded")

    profile_data = extract_profile(
        resume_text,
        api_key
    )

    st.subheader("Resume Preview")

    st.text_area(
        "Extracted Text",
        resume_text[:5000],
        height=300
    )

if st.button("Save Profile"):

    profile = {
    "roles": roles,
    "locations": locations,
    "resume_text": resume_text if resume else ""
    }

    save_profile(profile)

    st.success("Profile saved successfully")

saved_profile = load_profile()

if saved_profile:

    st.subheader("Saved Profile")

    st.json(saved_profile)

if saved_profile:

    st.write(
        f"Resume Characters: {len(saved_profile.get('resume_text',''))}"
    )
if resume:

    st.subheader("AI Extracted Profile")

    st.write(profile_data)
