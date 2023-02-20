from .. import lights

defaults = {
  'colors': [(170, 0, 255)],
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
    for x in range(self.app.num_pixels):
      color = self.colors[x % len(self.colors)]
      self.app.pixels[x] = color

    self.app.pixels.show()