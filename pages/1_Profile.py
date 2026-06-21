import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("."))

from service.resume_parser import extract_resume_text
from service.profile_manager import save_profile

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
from service.profile_manager import load_profile

saved_profile = load_profile()

if saved_profile:

    st.subheader("Saved Profile")

    st.json(saved_profile)
