from flask import Flask, request
from markupsafe import escape
import lights

import threading

runner = lights.Runner()

def lightThread():
  runner.run()

lt = threading.Thread(target=lightThread)
lt.start()

app = Flask(__name__)

@app.route("/off")
def all_off():
  runner.set_routine('', request.args)
  return {
    "name": "off"
  }

@app.route('/routine/<name>')
def run_routine(name):
  runner.set_routine(name, request.args)
  return {
    "name": name
  }