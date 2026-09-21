from flask import Flask, abort
app = Flask(__name__)
PROJECTS = {
    1: {"name": "Public Website Refresh", "data": "Routine project."},
    2: {"name": "ShadowVault", "data": "SHADOW{broken_portal_idor}\nNEXT: Analyze the captured network traffic."},
}

@app.get("/")
def index():
    return '<h1>NovaTech Internal Portal</h1><p>Project dashboard: <a href="/project/1">Project 1</a></p>'

@app.get("/project/<int:project_id>")
def project(project_id):
    item = PROJECTS.get(project_id)
    if not item:
        abort(404)
    # Intentionally vulnerable for the CTF: no authorization check.
    return f"<h2>{item['name']}</h2><pre>{item['data']}</pre>"

app.run(host="0.0.0.0", port=5000)
