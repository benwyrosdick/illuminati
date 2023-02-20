import random

from .. import lights
from . import routine

defaults = {
  'delay': 0.2,
  'colors': [
    lights.colors['violet'],
    lights.colors['violet'],
    lights.colors['black'],
    lights.colors['black'],
    lights.colors['black'],
    lights.colors['black']
  ],
  'sequence': 0,
  'reverse': False,
}

class Routine(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

  def tick(self):
    for i in range(self.app.num_pixels):
      if self.reverse:
        self.app.pixels[i] = self.colors[(i - self.sequence) % len(self.colors)]
      else:
        self.app.pixels[i] = self.colors[(i + self.sequence) % len(self.colors)]

    self.sequence += 1
    self.sequence %= len(self.colors)

    self.app.pixels.show()
