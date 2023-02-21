from .. import lights
from . import routine

defaults = {}

class Off(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

  def tick(self):
    self.app.pixels.fill(lights.colors['black'])
    self.app.pixels.show()