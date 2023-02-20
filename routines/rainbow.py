from .. import lights

defaults = {
  'delay': 0.06,
  'sequence': 0,
  'sequence_max': 150
}

class Routine():
  def __init__ (self, app, args={}):
    # defaults
    self.app = app
    self.args = args

    self.delay = self.getArg('delay')
    self.spread = self.getArg('spread')
    self.sequence = self.getArg('sequence')
    self.sequence_max = self.getArg('sequence_max')

  def config(self):
    return {
      'name': 'flicker',
      'delay': self.delay,
      'spread': self.spread,
      'sequence_max': self.sequence_max
    }
  
  def getArg(self, arg):
    if arg in self.args:
      return self.args[arg]
    elif arg in defaults:
      return defaults[arg]
    else:
      return None

  def tick(self):
    shift = 1.0 / self.sequence_max
    step = 1.0 / self.app.num_pixels

    for x in range(self.app.num_pixels):
      hue = self.sequence*shift + step*x
      hue = hue - int(hue)
      self.app.pixels[x] = lights.hls2rgb(hue, 0.5, 1)

    self.sequence += 1
    self.sequence %= self.sequence_max

    self.app.pixels.show()
