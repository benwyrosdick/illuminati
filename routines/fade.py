from .. import lights
from . import routine

defaults = {
  'delay': 0.1,
}

def color_diff(a, b, shift):
    return (
      int(a[0] - (a[0] - b[0]) * shift),
      int(a[1] - (a[1] - b[1]) * shift),
      int(a[2] - (a[2] - b[2]) * shift)
    )

class Fade(routine.Routine):
  def __init__(self, app, args):
    super().__init__(app, args, defaults)

    self.sequence_max = len(self.colors) * self.length

  def tick(self):
    self.increment_sequence()

    fade = int(self.length * 0.5)
    solid = self.length - fade

    color_index = self.sequence // self.length
    color_a = self.colors[color_index]
    color_b = self.colors[(color_index + 1) % len(self.colors)]

    pos = self.sequence % self.length
    if pos <= solid:
      self.app.pixels.fill(color_a)
    else:
      self.app.pixels.fill(color_diff(color_a, color_b, (pos - solid) / fade))

    self.app.pixels.show()
