from .. import lights
from . import routine

defaults = {
  'delay': 0.333,
  'sequence_max': 360,
}

class Cycle(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

  def tick(self):
    shift = 1.0 / self.sequence_max

    hue = self.sequence*shift
    hue %= 1.0
  
    self.app.pixels.fill(lights.hls2rgb(hue, 0.5, 1))

    self.increment_sequence()
    self.app.pixels.show()
