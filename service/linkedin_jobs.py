import json

def search_jobs(selected_roles):

    with open(
        "jobs.json",
        "r",
        encoding="utf-8"
    ) as f:

        jobs = json.load(f)

    return jobs
