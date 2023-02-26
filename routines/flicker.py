import random

from .. import lights
from . import routine

defaults = {
  'delay': 0.100,
  'colors': [ lights.colors['violet'] ],
  'spread': 15 / 360,
}

class Flicker(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

  def tick(self):
    for i in range(int(self.app.num_pixels * 0.1)):
      current_color = self.enumerated_colors[random.randint(0,len(self.enumerated_colors)-1)]
      current_hsv = lights.rgb2hsv(current_color)
      starting = current_hsv[0] - self.spread
      ending = current_hsv[0] + self.spread
      self.app.pixels[random.randint(0,self.app.num_pixels-1)] = lights.hsv2rgb(random.uniform(starting, ending)%1.0, current_hsv[1], current_hsv[2]*random.uniform(0.2, 1.0))

    self.app.pixels.show()
