import random

from .. import lights
from . import routine

defaults = {
  'delay': 0.075,
  'colors': [
    lights.colors['violet'],
  ],
  'length': 20
}

class Trails(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

    self.sequence_max = len(self.colors) * self.length

  def tick(self):
    for i in range(self.app.num_pixels):
      color = self.colors[((i + self.sequence) // self.length) % len(self.colors)]
      brightness = 1.0 - ((i + self.sequence) % self.length) * (1.0 / (self.length - 1))
      hsv = lights.rgb2hsv(color)
      self.app.pixels[i] = lights.hsv2rgb(hsv[0], hsv[1], brightness)

    self.increment_sequence()
    self.app.pixels.show()
