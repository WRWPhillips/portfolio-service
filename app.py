# module imports
from flask import *
from flask_cors import CORS 
import requests 
import os 

app = Flask(__name__)

url = "https://api.github.com/users/WRWPhillips/repos?per_page=100&sort=updated"
headers = {"Accept":"application/vnd.github.mercy-preview+json"}
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")

@app.route('/projects', methods=["GET"])
def getProjects():
    try:
        repos = requests.get(url, headers=headers, auth=(username, token)).json()
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)