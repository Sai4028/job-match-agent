import requests


def search_jobs(selected_roles):

    jobs = []

    try:

        response = requests.get(
            "https://www.arbeitnow.com/api/job-board-api"
        )

        data = response.json()

        for job in data.get("data", []):

            title = job.get("title", "")

            for role in selected_roles:

                if role.lower().split()[0] in title.lower():

                    jobs.append(
                        {
                            "title": job.get("title"),
                            "company": job.get("company_name"),
                            "location": job.get("location"),
                            "description": job.get("description"),
                            "apply_link": job.get("url")
                        }
                    )

        return jobs[:20]

    except Exception as e:

        return [
            {
                "title": "Error",
                "company": str(e),
                "location": "",
                "apply_link": ""
            }
        ]
