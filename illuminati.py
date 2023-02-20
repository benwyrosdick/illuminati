import neopixel
import random
import time

from . import lights
from .routines import off, flicker, rainbow, solid, chase

default_delay = 0.5

class Illuminati():
  def __init__ (self, num_pixels=50, brightness=0.2, pixel_order=neopixel.RGB):
    self.pixels = lights.get_board(num_pixels, auto_write=False, brightness=brightness, pixel_order=pixel_order)
    self.num_pixels = num_pixels

    self.routine = self.routine = off.Routine(self, {})
    self.delay = default_delay
  
  def set_routine(self, routine, args):
    hue_colors = list(map(lights.degrees_to_rgb, args['hues'])) if args['hues'] else []
    hex_colors = list(map(lights.hex2rgb, args['colors'])) if args['colors'] else []
    all_colors = hue_colors + hex_colors

    safe_args = {}
    if args['delay']:
      safe_args['delay'] = int(args['delay']) / 1000.0
    if len(all_colors):
      safe_args['colors'] = all_colors
    if args['spread']:
      safe_args['spread'] = lights.degrees_to_decimal(args['spread'])
    safe_args['reverse'] = args['reverse']

    if (routine == 'off'):
      self.routine = off.Routine(self, safe_args)
    if (routine == 'solid'):
      self.routine = solid.Routine(self, safe_args)
    if (routine == 'chase'):
      self.routine = chase.Routine(self, safe_args)
    elif (routine == 'flicker'):
      self.routine = flicker.Routine(self, safe_args)
    elif (routine == 'rainbow'):
      self.routine = rainbow.Routine(self, safe_args)

    self.delay = self.routine.getArg('delay') or default_delay

    return self.routine

  def run(self):
    while True:
      if self.routine:
        self.routine.tick()
      
      time.sleep(self.delay)
