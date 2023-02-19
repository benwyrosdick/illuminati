import neopixel
import random
import time

import lights

from routines import off

defaults = {
  "routine": 'off',
  "delay": 1,
  "hues": [0.5],
  "spread": 0.03,
  "sequence": 0,
  "sequence_max": 250
}

class Illuminati():
  def __init__ (self, num_pixels=50, brightness=0.2, pixel_order=neopixel.RGB):
    self.pixels = lights.get_board(num_pixels, auto_write=False, brightness=brightness, pixel_order=pixel_order)
    self.num_pixels = num_pixels

    # defaults
    self.routine = defaults['routine']
    self.delay = defaults['delay']
    self.hues = defaults['hues']
    self.spread = defaults['spread']
    self.sequence = defaults['sequence']
    self.sequence_max = defaults['sequence_max']
  
  def set_routine(self, routine, args):
    self.routine = routine
    
    # known options
    self.hues = list(map(lights.degrees_to_decimal, args['hues'])) if args['hues'] else self.hues or defaults['hues']
    self.delay = int(args['delay']) / 1000.0 if args['delay'] else self.delay or defaults['delay']
    self.spread = lights.degrees_to_decimal(args['spread']) if args['spread'] else self.spread or defaults['spread']

  def run(self):
    while True:
      if self.routine == 'off':
        self.pixels.fill((0,0,0))
      elif self.routine == 'solid':
        for x in range(self.num_pixels):
          hue = self.hues[x % len(self.hues)]
          self.pixels[x] = lights.hls2rgb(hue, 0.5, 1)
      elif self.routine == 'flicker':
        current_hue = self.hues[random.randint(0,len(self.hues)-1)]
        starting = current_hue - self.spread
        ending = current_hue + self.spread
        self.pixels[random.randint(0,self.num_pixels-1)] = lights.hls2rgb(random.uniform(starting, ending), random.uniform(0.05,0.5), 1)
      elif self.routine == 'rainbow':
        shift = 1.0 / self.sequence_max
        step = 1.0 / self.num_pixels
        for x in range(self.num_pixels):
          hue = self.sequence*shift + step*x
          hue = hue - int(hue)
          self.pixels[x] = lights.hls2rgb(hue, 0.5, 1)

      self.sequence += 1
      self.sequence %= self.sequence_max
      self.pixels.show()
      time.sleep(self.delay)
