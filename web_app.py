from rasa_core.channels.socketio import SocketIOInput
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.agent import Agent
from flask import Flask
from flask import render_template, jsonify, request
import requests

from urllib.request import urlopen
import json
import random
app = Flask(__name__)

@app.route('/')
def header():
    return render_template("index.html")

@app.route('/left-sidebar')
def left_sidebar():
    return render_template("left-sidebar.html")

@app.route('/right-sidebar')
def right_sidebar():
    return render_template("right-sidebar.html")

@app.route('/no-sidebar')
def no_sidebar():
    return render_template("no-sidebar.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/ask', methods=["POST"])
def ask():
    values = list(request.form.values())
    print(values[0])
    r = requests.post('http://localhost:5055/webhook', json={"message": values[0] })
    print(r.text)
    return "HI"

app.config["DEBUG"] = True
if __name__ == "__main__":
    # app.run(port=8000)
    app.run(debug=True)