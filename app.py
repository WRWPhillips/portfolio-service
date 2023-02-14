# module imports
from flask import *
from flask_cors import CORS 
import requests 
import os 

app = Flask(__name__)
CORS(app)

token = os.getenv("TOKEN")

url = "https://api.github.com/users/WRWPhillips/repos?per_page=100&sort=updated"
headers = {"Accept":"application/vnd.github.mercy-preview+json",
            "Authorization": token}

@app.route('/projects', methods=["GET"])
def getProjects():
    try:
        repos = requests.get(url, headers=headers).json()
        projects = []
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
            

if __name__ == '__main__':
    port = 8080
    app.run(host='0.0.0.0', port=8080, debug=True)
