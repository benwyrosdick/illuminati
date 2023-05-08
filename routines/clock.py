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

    # paint second hand
    second_hand_light = lights_per_block * second_hand_position
    leading_light = int(second_hand_light)
    trailing_light = int(second_hand_light + 1)
    trailing_light_intensity = second_hand_light - leading_light
    leading_light_intensity = 1 - trailing_light_intensity
    second_hand_light_color = lights.rgb2hsv(lights.colors['blue'])
    self.app.pixels[leading_light % self.app.num_pixels] = lights.hsv2rgb(second_hand_light_color[0], second_hand_light_color[1], second_hand_light_color[2]*leading_light_intensity)
    self.app.pixels[trailing_light % self.app.num_pixels] = lights.hsv2rgb(second_hand_light_color[0], second_hand_light_color[1], second_hand_light_color[2]*trailing_light_intensity)

    # paint minute and hour hands
    self.app.pixels[(self.app.top_light + int(lights_per_block * minute_hand_position)) % self.app.num_pixels] = lights.colors['green']
    self.app.pixels[(self.app.top_light + int(lights_per_block * hour_hand_position)) % self.app.num_pixels] = lights.colors['red']

    self.increment_sequence()
    self.app.pixels.show()
