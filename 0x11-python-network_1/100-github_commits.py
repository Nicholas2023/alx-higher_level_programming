#!/usr/bin/python3
"""
Here's a Python script that takes the repository name and
owner name as arguments and prints the last 10 commits
in the required format
"""
import requests
import sys


def fetch_commits(owner, repo):
    base_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'per_page': 10}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        commits = response.json()

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
    else:
        repository_name = sys.argv[1]
        owner_name = sys.argv[2]
        fetch_commits(owner_name, repository_name)
