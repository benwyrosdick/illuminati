from flask import Flask, request
from flask_cors import CORS

from .illuminati import Illuminati
from .lights import colors, themes

import threading

runner = Illuminati()

def illuminatiThread():
  runner.run()

it = threading.Thread(target=illuminatiThread)
it.start()

app = Flask(__name__)
CORS(app)

@app.route("/")
def status():
  return runner.routine.config()

@app.route("/off")
def all_off():
  args = _parse_args(request)
  routine = runner.set_routine('off', args)
  return routine.config()

@app.route('/routine/<name>')
def run_routine(name):
  args = _parse_args(request)
  routine = runner.set_routine(name, args)
  return routine.config()

def _parse_args(request):
  hues = request.args.getlist('hue')
  colors = request.args.getlist('color')
  delay = request.args.get('delay')
  spread = request.args.get('spread')
  length = request.args.get('length')
  reverse = request.args.get('reverse', default=False, type=bool)

  return {
    'hues': hues,
    'colors': colors,
    'delay': delay,
    'spread': spread,
    'length': length,
    'reverse': reverse
  }