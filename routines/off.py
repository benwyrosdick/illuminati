from .. import lights
from . import routine

defaults = {}

class Routine(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

  def tick(self):
    self.app.pixels.fill(lights.colors['black'])
    self.app.pixels.show()