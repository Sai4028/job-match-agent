import streamlit as st
from service.profile_manager import load_profile

profile = load_profile()

st.write(type(profile))

st.write(type(profile.get("ai_profile")))

st.write(profile.get("ai_profile"))
