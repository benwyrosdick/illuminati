from .. import lights

defaults = {}

class Routine():
  def __init__ (self, app, args={}):
    # defaults
    self.app = app
    self.args = args
  
  def config(self):
    return {
      'name': self.__class__.__name__.lower(),
      'args': self.args
    }

  def getArg(self, arg):
    if arg in self.args:
      return self.args[arg]
    elif arg in defaults:
      return defaults[arg]
    else:
      return None

  def tick(self):
    self.app.pixels.fill(lights.colors['black'])
    self.app.pixels.show()