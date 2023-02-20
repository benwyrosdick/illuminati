from .. import lights

base_defaults = {
  'delay': 0.1,
  'sequence': 0,
  'sequence_max': 50,
  'reverse': False
}

class Routine():
  def __init__ (self, app, args={}, defaults={}):
    # defaults
    self.app = app
    self.args = {**base_defaults, **defaults, **args}

    for key in self.args:
      self.__dict__[key] = self.args[key]
  
  def config(self):
    return {
      'name': self.__class__.__name__.lower(),
      'args': self.args
    }
  
  def increment_sequence(self):
    if self.reverse:
      self.sequence -= 1
    else:
      self.sequence += 1
    self.sequence %= self.sequence_max

  def tick(self):
    self.app.pixels.fill(lights.colors['black'])
    self.app.pixels.show()