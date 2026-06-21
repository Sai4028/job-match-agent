from service.remoteok_search import search_remoteok_jobs
import requests


def search_jobs(selected_roles):

    jobs = []

    try:

        response = requests.get(
            "https://www.arbeitnow.com/api/job-board-api"
        )

        data = response.json()

        product_keywords = [
            "product",
            "product manager",
            "product owner",
            "product lead",
            "head of product",
            "principal product",
            "group product",
            "technical product",
            "platform product",
            "ai product",
            "senior product"
        ]

        for job in data.get("data", []):

            title = job.get(
                "title",
                ""
            ).lower()

            description = job.get(
                "description",
                ""
            ).lower()

            if (
                any(
                    keyword in title
                    for keyword in product_keywords
                )
                or
                (
                    "product" in description
                    and (
                        "roadmap" in description
                        or "strategy" in description
                        or "stakeholder" in description
                        or "requirements" in description
                    )
                )
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

        print(
            f"Total Product Jobs Retrieved: {len(jobs)}"
        )

        remote_jobs = search_remoteok_jobs()

        all_jobs = jobs + remote_jobs
        
        return all_jobs[:30]
    except Exception as e:

        print(str(e))

        return [
            {
                "title": "Error",
                "company": str(e),
                "location": "",
                "description": "",
                "apply_link": ""
            }
        ]
