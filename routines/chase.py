import random

from .. import lights

defaults = {
  'delay': 0.2,
  'colors': [lights.colors['violet'], lights.colors['violet'], lights.colors['black'], lights.colors['black']],
  'sequence': 0
}

class Routine():
  def __init__ (self, app, args={}):
    # defaults
    self.app = app
    self.args = args

    self.delay = self.getArg('delay')
    self.colors = self.getArg('colors')
    self.sequence = self.getArg('sequence')

  def config(self):
    return {
      'name': 'chase',
      'delay': self.delay,
      'colors': self.colors
    }
  
  def getArg(self, arg):
    if arg in self.args:
      return self.args[arg]
    elif arg in defaults:
      return defaults[arg]
    else:
      return None

  def tick(self):
    for i in range(self.app.num_pixels):
      self.app.pixels[i] = self.colors[(i + self.sequence) % len(self.colors)]

    self.sequence += 1
    self.sequence %= len(self.colors)

    self.app.pixels.show()
