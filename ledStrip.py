from neopixel import *
from datetime import datetime
import time
import random
import argparse
import inspect
import sys
import json
import os
from utils import *
from config import *

class LedStrip:

    ###########################
    ########## Utils ##########
    ###########################

    def __init__(self, led_count):
        self.color = "#FF9300"
        self.LED_COUNT = led_count
        LED_PIN = STRIP_GPIO_PIN
        LED_FREQ_HZ = 800000
        LED_DMA = 10
        LED_BRIGHTNESS = 255
        LED_INVERT = False
        LED_CHANNEL = 0
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()
        red = Color(255,0,0)
        green = Color(0,255,0)
        blue = Color(0,0,255)

    def off(self, strip):
        off_color_value = [0,0,0]
        self.setSegment(off_color_value, 0, self.LED_COUNT)

    def powerDown(self, strip):
        colorWipe(strip, Color(0,0,0), 10)

    def masterColor(self, brightness, color):
        c = Color(color[0], color[1], color[2])
        r,g,b = convert_brightness(brightness, color[0], color[1], color[2])
        light_color = [r,g,b]
        self.color = c
        self.setSegment(light_color, 0, self.LED_COUNT)

    def setSegment(self, color, start, end):
        c = Color(color[0], color[1], color[2])
        for i in range(start, end):
            self.strip.setPixelColor(i, c)
        self.strip.show()

    def fade(self, color, step):
        co = Color(color[0], color[1], color[2])

        if step == -1:
            b, c = -1, 255
        else:
            c,b = 0, 255
        for j in range(c, b, step):
            for i in range(0, self.strip.numPixels()):
                self.strip.setPixelColor(i,co)
            time.sleep(1/1000)
            self.strip.show()

    def fadeIn(self, color):
        self.fade(color, -1)

    def fadeOut(self, color):
        self.fade(color, 1)

    def setDualColor(self, color1, color2):
        c1 = Color(color1[0], color1[1], color1[2])
        c2 = Color(color2[0], color2[1], color2[2])
        for i in range(0, self.strip.numPixels()):
            if (i%2 == 0):
                self.strip.setPixelColor(i, c1)
            else:
                self.strip.setPixelColor(i, c2)
        self.strip.show()


    ###########################
    ######### Effects #########
    ###########################

    def theaterChase(self, color, wait_ms=50):
        while True:
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, color)
                self.strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)

    def colorWipe(self, color, wait_ms=50):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms/1000)

    def wheel(self, pos):
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(self, wait_ms=20, iterations=100):
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.wheel((i+j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def rainbowCycle(self, wait_ms=20, iterations=500):
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def theaterChaseRainbow(self, wait_ms=50):
        for j in range(256):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, self.wheel((i+j) % 255))
                self.strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)

    # def heartbeat(self):
    #    red = [255, 0, 0]
    #    for i in range (0,50):
    #        self.fadeIn(red)
    #        self.fadeOut(red)
    #        time.sleep(0.5)

    def fade_hit(self, start, end, color):
        iterations = 50.0

        for j in range(int(iterations)):
            d = iterations - j
            multiplier = d/iterations
            colour = Color(int(color[0]*multiplier*multiplier), int(color[1]*multiplier*multiplier), int(color[2]*multiplier*multiplier))

            for i in range(start, end):
                self.strip.setPixelColor(i, colour)
            time.sleep(1/100)
            self.strip.show()

    def setPixel(self, pixel, color):
        c = Color(color[0], color[1], color[2])
        self.strip.setPixelColor(pixel, c)

    def stripShow(self):
        self.strip.show()
