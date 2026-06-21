import streamlit as st
from service.profile_manager import load_profile

st.title("Job Search")

profile = load_profile()

st.write(profile)
