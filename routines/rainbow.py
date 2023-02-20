from .. import lights
from . import routine

defaults = {
  'delay': 0.06,
  'sequence': 0,
  'sequence_max': 150,
  'reverse': False
}

class Routine(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

  def tick(self):
    shift = 1.0 / self.sequence_max
    step = 1.0 / self.app.num_pixels

    for x in range(self.app.num_pixels):
      hue = self.sequence*shift

      if self.reverse:
        hue -= step*x        
      else:
        hue += step*x

      hue %= 1.0
      self.app.pixels[x] = lights.hls2rgb(hue, 0.5, 1)

    self.sequence += 1
    self.sequence %= self.sequence_max

    self.app.pixels.show()
