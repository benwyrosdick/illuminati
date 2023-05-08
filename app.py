from flask import Flask, request
from flask_cors import CORS

from .illuminati import Illuminati
from .lights import colors, themes

import threading
import yaml
import os

configPath = os.path.expanduser('~') + "/illuminati.yaml"
config = {}

if (os.path.isfile(configPath)):
  with open(configPath, 'r') as confFile:
      config = yaml.load(confFile, Loader=yaml.FullLoader)

num_pixels = config.get('num_pixels', 50)
runner = Illuminati(
  num_pixels=num_pixels,
  north_light=config.get('north_light', 0),
  top_light=config.get('top_light', 0),
  # top_right_light=config.get('top_right_light', num_pixels/4-1),
  # bottom_right_light=config.get('bottom_right_light', num_pixels/4*2-1),
  # bottom_left_light=config.get('bottom_left_light', num_pixels/4*3-1),
  # top_left_light=config.get('top_left_light', num_pixels-1),
  direction=config.get('direction', 'cw')
)

def illuminatiThread():
  runner.run()

it = threading.Thread(target=illuminatiThread)
it.start()

app = Flask(__name__)
CORS(app)

@app.route("/")
def status():
  return {
    'routine': runner.routine.config(),
    'routines': ['off', 'chase', 'cycle', 'fade', 'flicker', 'rainbow', 'solid', 'trails', 'twinkle', 'clock'],
    'colors': colors,
    'themes': themes
  }

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
  colors = request.args.getlist('color')
  brightness = request.args.get('brightness')
  delay = request.args.get('delay')
  spread = request.args.get('spread')
  length = request.args.get('length')
  spacing = request.args.get('spacing')
  surround_spacing = request.args.get('surround_spacing')
  reverse = request.args.get('reverse', default=False, type=bool)

  return {
    'colors': colors,
    'brightness': brightness,
    'delay': delay,
    'spread': spread,
    'length': length,
    'spacing': spacing,
    'surround_spacing': surround_spacing,
    'reverse': reverse
  }
