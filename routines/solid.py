from .. import lights

defaults = {
  'colors': [lights.colors['violet']],
}

class Routine():
  def __init__ (self, app, args={}):
    # defaults
    self.app = app
    self.args = args

    self.colors = self.getArg('colors')

  def config(self):
    return {
      'name': 'solid',
      'colors': self.colors,
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
      color = self.colors[i % len(self.colors)]
      self.app.pixels[i] = color

    self.app.pixels.show()