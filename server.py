from flask import *
from flask_cors import CORS
from config import *
import requests
import os

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run()
# remember to add env variables in a minute
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
@app.route('/projects', methods=["GET"])
def getProjects():
    try:
        url = "https://api.github.com/users/WRWPhillips/repos?per_page=100"
        headers = {"Accept":"application/vnd.github.mercy-preview+json"}
        repos = requests.get(url, headers=headers, auth=(USERNAME,TOKEN)).json()
        projects = []
        print(repos)
        for repo in repos: 
            if repo["stargazers_count"] >= 1: 
                project = {
                    "id": repo["id"],
                    "name": repo["name"],
                    "url": repo["html_url"],
                    "description": repo["description"],
                    "topics": repo["topics"],
                    "language": repo["language"]
                }
                projects.append(project)
        return {"projects": projects, "error": False}
    except Exception as e:
        return {"error": True, "message": str(e)}, 500
