import neopixel
import random
import time

import lights

from routines import off

defaults = {
  "routine": 'off',
  "delay": 1,
  "colors": [(255,0,0)],
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
    self.colors = defaults['colors']
    self.spread = defaults['spread']
    self.sequence = defaults['sequence']
    self.sequence_max = defaults['sequence_max']
  
  def set_routine(self, routine, args):
    self.routine = routine
    
    # known options
    hue_colors = list(map(lights.degrees_to_rgb, args['hues'])) if args['hues'] else []
    hex_colors = list(map(lights.hex2rgb, args['colors'])) if args['colors'] else []
    all_colors = hue_colors + hex_colors
    self.colors = all_colors if len(all_colors) > 0 else self.colors or defaults['colors']
    self.delay = int(args['delay']) / 1000.0 if args['delay'] else self.delay or defaults['delay']
    self.spread = lights.degrees_to_decimal(args['spread']) if args['spread'] else self.spread or defaults['spread']

    return {
      'routine': self.routine,
      'delay': self.delay,
      'colors': self.colors,
      'spread': self.spread,
      'sequence_max': self.sequence_max,
    }

  def run(self):
    while True:
      if self.routine == 'off':
        self.pixels.fill((0,0,0))
      elif self.routine == 'solid':
        for x in range(self.num_pixels):
          color = self.colors[x % len(self.colors)]
          self.pixels[x] = color
      elif self.routine == 'flicker':
        current_color = self.colors[random.randint(0,len(self.colors)-1)]
        current_hsv = lights.rgb2hsv(current_color)
        starting = current_hsv[0] - self.spread
        ending = current_hsv[0] + self.spread
        self.pixels[random.randint(0,self.num_pixels-1)] = lights.hsv2rgb(random.uniform(starting, ending)%1.0, current_hsv[1], random.uniform(0.2, 1.0))
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
