from .. import lights

base_defaults = {
  'colors': [],
  'delay': 0.1,
  'brightness': 0.5,
  'sequence': 0,
  'sequence_max': 50,
  'length': 1,
  'spread': 0,
  'spacing': 0,
  'surround_spacing': 0,
  'reverse': False
}

class Routine():
  def __init__ (self, app, args={}, defaults={}):
    # defaults
    self.app = app
    self.args = {**base_defaults, **defaults, **args}

    for key in self.args:
      self.__dict__[key] = self.args[key]
    self.enumerate_colors()
  
  def config(self):
    args = {**self.args}
    args['delay'] = int(args['delay'] * 1000)
    args['brightness'] = int(args['brightness'] * 100)
    if 'spread' in args:
      args['spread'] = int(args['spread'] * 360)

    return {
      'name': self.__class__.__name__.lower(),
      'args': args
    }
  
  def enumerate_colors(self):
    colors = []

    for color in self.colors:
      for l in range(self.length):
        colors.append(color)
      for s in range(self.spacing):
        colors.append(lights.colors['black'])
    for s in range(self.surround_spacing):
      colors.append(lights.colors['black'])

    if len(colors) == 0:
      colors.append(lights.colors['black'])
    
    self.enumerated_colors = colors
  
  def increment_sequence(self):
    if self.sequence_max > 0:
      if self.reverse:
        self.sequence -= 1
      else:
        self.sequence += 1
      self.sequence %= self.sequence_max

  def tick(self):
    self.app.pixels.fill(lights.colors['black'])
    self.app.pixels.show()