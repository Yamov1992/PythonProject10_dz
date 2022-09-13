import utils
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")

def index():

    candidates = utils.get_candidates_all()
    result = "<br>"

    for candidate in candidates:
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"
        result += ""

    return f"<pre> {result} </pre>"

@app.route("/candidate/<int:pk>")

def get_candidate(pk):

    candidate = utils.get_candidate_by_pk(pk)
    result = "<br>"
    result += candidate["name"] + "<br>"
    result += candidate["position"] + "<br>"
    result += candidate["skills"] + "<br>"
    result += "<br>"

    return f"""
        <img src="({candidate["picture"]})">
        <pre> {result} </pre>
    """

@app.route("/candidate/<skill>")

def candidate_skills(skill):

    candidates = utils.get_candidates_by_skill(skill.lower())
    result = "<br>"

    for candidate in candidates:
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"
        result += ""

    return f"<pre> {result} </pre>"

app.run(debug = True)