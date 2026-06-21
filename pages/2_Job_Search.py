import streamlit as st
from service.profile_manager import load_profile

st.title("Job Search")

profile = load_profile()

if not profile:
    st.warning("Please create your profile first.")
    st.stop()

ai_profile = profile.get("ai_profile", {})

st.subheader("Recommended Roles")

recommended_roles = ai_profile.get(
    "recommended_roles",
    []
)

selected_roles = []

for role in recommended_roles:

    if st.checkbox(
        role,
        value=True
    ):
        selected_roles.append(role)

st.subheader("Locations")

locations = profile.get(
    "locations",
    ""
)

st.write(locations)

st.divider()

st.write("Selected Roles")

st.write(selected_roles)

if st.button("Search Jobs"):
    st.success(
        f"Searching jobs for {len(selected_roles)} roles..."
    )
