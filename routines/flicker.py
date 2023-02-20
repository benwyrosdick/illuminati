import random

from .. import lights

defaults = {
  'delay': 0.025,
  'colors': [lights.colors['violet']],
  'spread': 15 / 360,
}

class Routine():
  def __init__ (self, app, args={}):
    # defaults
    self.app = app
    self.args = args

    self.delay = self.getArg('delay')
    self.colors = self.getArg('colors')
    self.spread = self.getArg('spread')

  def config(self):
    return {
      'name': 'flicker',
      'delay': self.delay,
      'colors': self.colors,
      'spread': self.spread
    }
  
  def getArg(self, arg):
    if arg in self.args:
      return self.args[arg]
    elif arg in defaults:
      return defaults[arg]
    else:
      return None

  def tick(self):
    current_color = self.colors[random.randint(0,len(self.colors)-1)]
    current_hsv = lights.rgb2hsv(current_color)
    starting = current_hsv[0] - self.getArg('spread')
    ending = current_hsv[0] + self.getArg('spread')
    self.app.pixels[random.randint(0,self.app.num_pixels-1)] = lights.hsv2rgb(random.uniform(starting, ending)%1.0, current_hsv[1], random.uniform(0.2, 1.0))

    self.app.pixels.show()
