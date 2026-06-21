import sys
import os

sys.path.append(os.path.abspath("."))

from services.resume_parser import extract_resume_text

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
    st.success("Profile saved successfully")
