import requests


def search_jobs(selected_roles):

    jobs = []

    try:

        response = requests.get(
            "https://www.arbeitnow.com/api/job-board-api"
        )

        data = response.json()

        product_keywords = [
            "product manager",
            "product owner",
            "product lead",
            "head of product",
            "principal product manager",
            "group product manager",
            "senior product manager",
            "ai product manager",
            "technical product manager",
            "platform product manager"
        ]

        for job in data.get("data", []):

            title = job.get(
                "title",
                ""
            ).lower()

            if any(
                keyword in title
                for keyword in product_keywords
            ):

                jobs.append(
                    {
                        "title": job.get(
                            "title",
                            ""
                        ),
                        "company": job.get(
                            "company_name",
                            ""
                        ),
                        "location": job.get(
                            "location",
                            ""
                        ),
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

        return jobs[:20]

    except Exception as e:

        return [
            {
                "title": "Error",
                "company": str(e),
                "location": "",
                "description": "",
                "apply_link": ""
            }
        ]
