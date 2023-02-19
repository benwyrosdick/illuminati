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
