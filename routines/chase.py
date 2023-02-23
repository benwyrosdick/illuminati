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
}

class Chase(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

    self.sequence_max = len(self.enumerated_colors)

  def tick(self):
    for i in range(self.app.num_pixels):
      self.app.pixels[i] = self.enumerated_colors[(i + self.sequence) % len(self.enumerated_colors)]

    self.increment_sequence()
    self.app.pixels.show()
