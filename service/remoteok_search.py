import requests


def search_remoteok_jobs():

    jobs = []

    try:

        response = requests.get(
            "https://remoteok.com/api"
        )

        data = response.json()

        for job in data:

            if not isinstance(job, dict):
                continue

            jobs.append(
                {
                    "title": job.get(
                        "position",
                        ""
                    ),
                    "company": job.get(
                        "company",
                        ""
                    ),
                    "location": "Remote",
                    "description": job.get(
                        "description",
                        ""
                    ),
                    "apply_link": job.get(
                        "url",
                        ""
                    )
                }
            )

        return jobs

    except Exception as e:

        print(str(e))

        return []
