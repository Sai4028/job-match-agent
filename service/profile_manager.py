import json
import os

PROFILE_PATH = "data/profile.json"

def save_profile(profile_data):

    os.makedirs("data", exist_ok=True)

    with open(PROFILE_PATH, "w") as f:
        json.dump(profile_data, f, indent=4)

def load_profile():

    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, "r") as f:
            return json.load(f)

    return None
