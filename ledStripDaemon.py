import time
import json
from config.config import *
from ledStrip import *
from config.pixelMap import *
from animations.hitAnimations import *

# class LedDrumRunner(midi_note_queue):
#     def __init__(self):
#         midi_queue = midi_note_queue

#     def getStripSegment(note):
#         drum_name = MIDI_NOTE_INDEX[note]
#         start = LED_DRUM_INDEX[drum_name][0]
#         end = LED_DRUM_INDEX[drum_name][1]
#         return start, end


def getStripSegment(note):
    drum_name = MIDI_NOTE_INDEX[note]
    start = LED_DRUM_INDEX[drum_name][0]
    end = LED_DRUM_INDEX[drum_name][1]
    return start, end

def initStripValues(led_count):
    current_strip_values = {}
    for i in range(LED_COUNT):
        current_strip_values[i] = [0,0,0]

    return current_strip_values

def runStartupAnimation(led_strip):
    # Horizontal wipe
    g = len(pixel_map)
    for y in range(0, g/2):
        numbers = pixel_map[(g/2) + y] + pixel_map[(g/2) - y]
        for j in numbers:
            led_strip.setPixel(j, [255, 255, 255])
        led_strip.stripShow()
        for k in range(600):
            led_strip.setPixel(k, [0,0,0])
    led_strip.stripShow()
    for y in range(1, g/2):
        r = (g/2) - y
        numbers = pixel_map[(g/2) + r] + pixel_map[(g/2) - r]
        for j in numbers:
            led_strip.setPixel(j, [255, 255, 255])
        led_strip.stripShow()
        for k in range(600):
            led_strip.setPixel(k, [0,0,0])
        led_strip.stripShow()
    for t in range(0, 250, 10):
        u = 250 - t
        led_strip.setSegment([u,0,0], 0, LED_COUNT)

    # Load color palette
    with open('config/accentColors.json') as json_file:
        colors = json.load(json_file)

def ledStripDaemon(midi_note_queue):
    led_strip = LedStrip(LED_COUNT, STRIP_GPIO_PIN)
    current_strip_values = initStripValues(LED_COUNT)

    while True:
        try:
            midi_hit = midi_note_queue.get_nowait()

            if midi_hit["animation"]:
                if midi_hit["animation_type"] == 'startup':
                    runStartupAnimation(led_strip)
                elif midi_hit["animation_type"] == 'rainbow':
                    led_strip.rainbow(20,1)
                    led_strip.setSegment([u,0,0], 0, LED_COUNT)
                continue

            if midi_hit["type"] == "accent":
                start,end = 0, LED_COUNT
                hit_color = colors["accent_hit_1"]
            else:
                start, end = getStripSegment(j["note"])

            # Set Color
            if midi_hit["type"] == "kick":
                hit_color = colors["kick"]
            elif midi_hit["type"] == "snare":
                hit_color = colors["snare"]
            elif midi_hit["type"] == "pad":
                hit_color = colors["pad"]
            elif midi_hit["type"] == "cymbal":
                hit_color = colors["cymbal"]
            elif midi_hit["type"] == "accent_1":
                hit_color = colors["accent_hit_1"]
            elif midi_hit["type"] == "accent_2":
                hit_color = colors["accent_hit_2"]

                #TODO add switch statement

            # Modify Brightness
            if int(midi_hit["velocity"]) > 80:
                mul = 1
            elif int(midi_hit["velocity"]) > 20:
                mul = midi_hit["velocity"]/80.0
            else:
                mul = 0.2
            hit_color = [int(hit_color[0]*mul), int(hit_color[1]*mul),int(hit_color[2]*mul)]


            for k in range(end-start):
                current_strip_values[k + start] = hit_color

            for i in range(len(current_strip_values)):
                r = current_strip_values[i][0]
                g = current_strip_values[i][1]
                b = current_strip_values[i][2]
                color = [g, r, b]
                led_strip.setPixel(i, color)
                current_strip_values[i] = linearFade(r, g, b)
            led_strip.stripShow()
        except:
            for i in range(len(current_strip_values)):
                r = current_strip_values[i][0]
                g = current_strip_values[i][1]
                b = current_strip_values[i][2]
                color = [g, r, b]
                led_strip.setPixel(i, color)
                current_strip_values[i] = linearFade(r, g, b)
            led_strip.stripShow()
