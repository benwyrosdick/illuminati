import board
import neopixel
import colorsys
import random
import time

colors = {
    'red': (255,0,0),
    'orange': (255,127,0),
    'yellow': (255,255,0),
    'green': (0,255,0),
    'blue': (0,0,255),
    'indigo': (75,0,130),
    'violet': (143,0,255),
    'white': (255,255,255),
    'black': (0,0,0)
}

themes = {
    'mardi_gras': [(0,255,0),(255,255,0),(128,0,255)],
    'rainbow': [(255,0,0),(255,127,0),(255,255,0),(0,255,0),(0,0,255),(128,0,255),(255,0,255)],
    'xmas': [(255,0,0),(0,255,0),(255,255,255)],
    'easter': [(0,255,255),(0,255,128),(0,255,0),(255,0,255),(255,255,0)],
    'rgb': [(255,0,0),(0,255,0),(0,0,255)],
    'auburn': [(229,96,0),(11,35,128)]
}

def decode_color(color):
    if color in themes:
        return [*themes[color]]
    elif color in colors:
        return [colors[color]]
    elif len(color) == 6:
        return [hex2rgb(color)]
    else:
        return [degrees_to_rgb(color)]

def get_board(num_pixels=50, auto_write=False, brightness=0.5, pixel_order=neopixel.GRBW):
    print(pixel_order)
    print(neopixel.RGBW)
    print(neopixel.GRBW)
    return neopixel.NeoPixel(board.D18, num_pixels, bbp=4, auto_write=auto_write, brightness=brightness, pixel_order=pixel_order)

def hls2rgb(h,l,s):
    return tuple(round(i * 255) for i in colorsys.hls_to_rgb(h,l,s))

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v/255))

def hex2rgb(hex):
    lv = len(hex)
    return tuple(int(hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb2hsv(rgb):
    return colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])

def randomList(items):
    return items[random.randint(0, len(items)-1)]

def randomColor():
    h = random.uniform(0,1)
    l = random.uniform(0,0.5)
    s = 1
    return hls2rgb(h,l,s)

def degrees_to_decimal(deg):
    return float(deg) / 360.0

def degrees_to_rgb(deg):
    hue = degrees_to_decimal(deg)
    return hls2rgb(hue, 0.5, 1)
