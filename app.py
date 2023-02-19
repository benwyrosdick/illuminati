from flask import Flask, request
from markupsafe import escape
import illuminati

import threading

runner = illuminati.Illuminati()

def illuminatiThread():
  runner.run()

it = threading.Thread(target=illuminatiThread)
it.start()

app = Flask(__name__)

@app.route("/off")
def all_off():
  args = _parse_args(request)
  runner.set_routine('', args)
  return {
    "name": "off",
    'args': args
  }

@app.route('/routine/<name>')
def run_routine(name):
  args = _parse_args(request)
  runner.set_routine(name, args)
  return {
    "name": name,
    'args': args
  }

def _parse_args(request):
  hues = request.args.getlist('hue')
  delay = request.args.get('delay')
  spread = request.args.get('spread')

  return {
    'hues': hues,
    'delay': delay,
    'spread': spread
  }