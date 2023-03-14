import neopixel
import random
import time

from . import lights
from .routines import off, flicker, rainbow, solid, chase, twinkle, trails, cycle, fade

default_delay = 0.5
tick_speed = 0.005
default_brightness=0.5
num_pixels=50
pixel_order=neopixel.RGB

class Illuminati():
  def __init__ (self):
    self.pixels = lights.get_board(num_pixels, auto_write=False, brightness=default_brightness, pixel_order=pixel_order)
    self.num_pixels = num_pixels

    self.routine = self.routine = off.Off(self, {})
    self.delay = default_delay
    self.last_tick = 0
  
  def set_routine(self, routine, args):
    # build args
    safe_args = {}
    if args['brightness']:
      safe_args['brightness'] = int(args['brightness']) / 100.0
      self.pixels = lights.get_board(num_pixels, auto_write=False, brightness=safe_args['brightness'], pixel_order=pixel_order)
    if args['delay']:
      safe_args['delay'] = int(args['delay']) / 1000.0
    if args['colors']:
      safe_args['colors'] = sum(list(map(lights.decode_color, args['colors'])), [])
    if args['spread']:
      safe_args['spread'] = lights.degrees_to_decimal(args['spread'])
    if args['length']:
      safe_args['length'] = int(args['length'])
    if args['spacing']:
      safe_args['spacing'] = int(args['spacing'])
    if args['surround_spacing']:
      safe_args['surround_spacing'] = int(args['surround_spacing'])
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
    elif (routine == 'trails'):
      self.routine = trails.Trails(self, safe_args)
    elif (routine == 'rainbow'):
      self.routine = rainbow.Rainbow(self, safe_args)
    elif (routine == 'cycle'):
      self.routine = cycle.Cycle(self, safe_args)
    elif (routine == 'fade'):
      self.routine = fade.Fade(self, safe_args)

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
