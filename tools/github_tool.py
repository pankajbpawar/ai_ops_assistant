import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def search_repositories(query, limit=5):
    url = "https://api.github.com/search/repositories"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return {"error": "GitHub API failed"}

    data = response.json()
    repos = []

    for item in data["items"]:
        repos.append({
            "name": item["name"],
            "stars": item["stargazers_count"],
            "url": item["html_url"]
        })

    return repos
