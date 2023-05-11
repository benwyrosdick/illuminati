from .. import lights
from . import routine

defaults = {}

class Solid(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

  def tick(self):
    for i in range(self.app.num_pixels):
      color = self.enumerated_colors[i % len(self.enumerated_colors)]
      self.app.pixels[i] = (255,0,0,128)

    self.app.pixels.show()