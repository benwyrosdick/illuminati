import neopixel
import random
import time

from . import lights
from .routines import off, flicker, rainbow, solid, chase, twinkle

default_delay = 0.5
tick_speed = 0.005

class Illuminati():
  def __init__ (self, num_pixels=50, brightness=0.2, pixel_order=neopixel.RGB):
    self.pixels = lights.get_board(num_pixels, auto_write=False, brightness=brightness, pixel_order=pixel_order)
    self.num_pixels = num_pixels

    self.routine = self.routine = off.Off(self, {})
    self.delay = default_delay
    self.last_tick = 0
  
  def set_routine(self, routine, args):
    hue_colors = list(map(lights.degrees_to_rgb, args['hues'])) if args['hues'] else []
    hex_colors = list(map(lights.hex2rgb, args['colors'])) if args['colors'] else []
    all_colors = hue_colors + hex_colors

    # build args
    safe_args = {}
    if args['delay']:
      safe_args['delay'] = int(args['delay']) / 1000.0
    if len(all_colors):
      safe_args['colors'] = all_colors
    if args['spread']:
      safe_args['spread'] = lights.degrees_to_decimal(args['spread'])
    safe_args['reverse'] = args['reverse']

    if 'sequence' in self.routine.__dict__:
      safe_args['sequence'] = self.routine.sequence

    # Select routine
    if (routine == 'off'):
      self.routine = off.Off(self, safe_args)
    if (routine == 'solid'):
      self.routine = solid.Solid(self, safe_args)
    if (routine == 'chase'):
      self.routine = chase.Chase(self, safe_args)
    elif (routine == 'flicker'):
      self.routine = flicker.Flicker(self, safe_args)
    elif (routine == 'twinkle'):
      self.routine = twinkle.Twinkle(self, safe_args)
    elif (routine == 'rainbow'):
      self.routine = rainbow.Rainbow(self, safe_args)

    self.delay = self.routine.delay

    return self.routine

  def run(self):
    while True:
      now = time.time()

      if now - self.last_tick > self.delay:
        self.last_tick = now
        
        if self.routine:
          self.routine.tick()
      
      time.sleep(tick_speed)
