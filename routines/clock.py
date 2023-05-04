from .. import lights
from . import routine

import datetime

defaults = {
  'delay': 0.333,
  'sequence_max': 360,
}

class Clock(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

  def tick(self):
    now = datetime.datetime.now()

    hour_hand_position = (now.hour % 12) + (now.minute / 60)
    minute_hand_position = (now.minute / 5)
    second_hand_position = (now.second / 5)
    lights_per_block = int(self.app.num_pixels / 12)

    self.app.pixels.fill(lights.colors['black'])
    self.app.pixels[(self.app.top_light + int(lights_per_block * hour_hand_position)) % self.app.num_pixels] = self.enumerated_colors[lights.colors['red']]
    self.app.pixels[(self.app.top_light + int(lights_per_block * minute_hand_position)) % self.app.num_pixels] = self.enumerated_colors[lights.colors['green']]
    self.app.pixels[(self.app.top_light + int(lights_per_block * second_hand_position)) % self.app.num_pixels] = self.enumerated_colors[lights.colors['blue']]

    self.increment_sequence()
    self.app.pixels.show()
