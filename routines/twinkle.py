import random

from .. import lights
from . import routine

defaults = {
  'delay': 0.100,
  'colors': [lights.colors['violet']],
}

class Twinkle(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

  def tick(self):
    for i in range(int(self.app.num_pixels * 0.1)):
      current_pos = random.randint(0,self.app.num_pixels-1)
      current_color = self.enumerated_colors[current_pos % len(self.enumerated_colors)]
      current_hsv = lights.rgb2hsv(current_color)
      self.app.pixels[current_pos] = lights.hsv2rgb(current_hsv[0], current_hsv[1], current_hsv[2]*random.uniform(0.2, 1.0))

    self.app.pixels.show()
