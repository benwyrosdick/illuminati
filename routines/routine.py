from .. import lights

class Routine():
  def __init__ (self, app, args={}, defaults={}):
    # defaults
    self.app = app
    self.args = {**defaults, **args}

    for key in self.args:
      self.__dict__[key] = self.args[key]
  
  def config(self):
    return {
      'name': self.__class__.__name__.lower(),
      'args': self.args
    }

  def tick(self):
    self.app.pixels.fill(lights.colors['black'])
    self.app.pixels.show()