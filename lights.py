import board
import neopixel
import colorsys
import random
import time

def get_board(num_pixels=50, auto_write=False, brightness=0.2, pixel_order=neopixel.RGB):
    return neopixel.NeoPixel(board.D18, num_pixels, auto_write=auto_write, brightness=brightness, pixel_order=pixel_order)

def hls2rgb(h,l,s):
    return tuple(round(i * 255) for i in colorsys.hls_to_rgb(h,l,s))

def randomList(items):
    return items[random.randint(0, len(items)-1)]

def randomColor():
    h = random.uniform(0,1)
    l = random.uniform(0,0.5)
    s = 1
    return hls2rgb(h,l,s)

def degrees_to_decimal(deg):
    return float(deg) / 360.0

class Runner():
    def __init__ (self, num_pixels=50, brightness=0.2, pixel_order=neopixel.RGB):
        self.pixels = get_board(num_pixels, auto_write=False, brightness=brightness, pixel_order=pixel_order)
        self.num_pixels = num_pixels

        # defaults
        self.routine = 'off'
        self.delay = 1
        self.hues = [0.5]
        self.spread = 0.03
        self.sequence = 0
        self.sequence_max = 250
    
    def set_routine(self, routine, args):
        self.routine = routine
        
        # known options
        hues = args.getlist('hue')
        if hues:
            self.hues = list(map(degrees_to_decimal, hues))

        delay = args.get('delay')
        if delay:
            self.delay = int(delay) / 1000.0

        spread = args.get('spread')
        if spread:
            self.spread = degrees_to_decimal(spread)

    def run(self):
        while True:
            if self.routine == 'off':
                self.pixels.fill((0,0,0))
            elif self.routine == 'solid':
                for x in range(self.num_pixels):
                    hue = self.hues[x % len(self.hues)]
                    self.pixels[x] = hls2rgb(hue, 0.5, 1)
            elif self.routine == 'flicker':
                current_hue = self.hues[random.randint(0,len(self.hues)-1)]
                starting = current_hue - self.spread
                ending = current_hue + self.spread
                self.pixels[random.randint(0,self.num_pixels-1)] = hls2rgb(random.uniform(starting, ending), random.uniform(0.1,0.5), 1)
            elif self.routine == 'rainbow':
                shift = 1.0 / self.sequence_max
                step = 1.0 / self.num_pixels
                for x in range(self.num_pixels):
                    hue = self.sequence*shift + step*x
                    hue = hue - int(hue)
                    self.pixels[x] = hls2rgb(hue, 0.5, 1)

            self.sequence += 1
            self.sequence %= self.sequence_max
            self.pixels.show()
            time.sleep(self.delay)

