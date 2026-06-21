import streamlit as st

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

if st.button("Save Profile"):
    st.success("Profile saved successfully")
