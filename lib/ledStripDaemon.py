from lib.ledStrip import *
from utils.utils import *
from config.config import *
from config.pixelMap import *
from animations.hitAnimations import *

def getStripSegmentIndex(note):
    start = DRUMKIT_CONFIG[note]["led_index"][0]
    end = DRUMKIT_CONFIG[note]["led_index"][1]
    return start, end

def initStripValues(led_count):
    current_strip_values = {}
    for i in range(LED_COUNT):
        current_strip_values[i] = [0,0,0]

    return current_strip_values

def runStartupAnimation(led_strip):
    # Horizontal wipe center to sides
    map_length = len(pixel_map)
    for i in range(0, map_length/2):
        numbers = pixel_map[(map_length/2) + i] + pixel_map[(map_length/2) - i]
        for pixel_on in numbers:
            led_strip.setPixel(pixel_on, [255, 255, 255])
        led_strip.stripShow()
        for pixel_off in range(LED_COUNT):
            led_strip.setPixel(pixel_off, [0,0,0])
    led_strip.stripShow()

    # Horizontal wipe sides to center
    for y in range(1, map_length/2):
        r = (map_length/2) - y
        numbers = pixel_map[(map_length/2) + r] + pixel_map[(map_length/2) - r]
        for pixel_on in numbers:
            led_strip.setPixel(pixel_on, [255, 255, 255])
        led_strip.stripShow()
        for pixel_off in range(LED_COUNT):
            led_strip.setPixel(pixel_off, [0,0,0])
        led_strip.stripShow()

    # White flash fade out
    for brightness_step in range(0, 250, 10):
        brightness_value = 250 - brightness_step
        led_strip.setSegment([brightness_value,0,0], 0, LED_COUNT)

def runAnimation(led_strip, animation_type):
    if (animation_type == 'startup'):
        runStartupAnimation(led_strip)
    # elif (animation_type== 'rainbow'):
        # led_strip.rainbow(20,1)
        # led_strip.setSegment([u,0,0], 0, LED_COUNT)
        #TODO


def ledStripDaemon(midi_note_queue):
    led_strip = LedStrip(LED_COUNT, STRIP_GPIO_PIN)
    current_strip_values = initStripValues(LED_COUNT)
    colours = read_json_file('config/accentColours.json')

    while True:
        try:
            midi_hit = midi_note_queue.get_nowait()

            if midi_hit["animation"]:
                runAnimation(led_strip, midi_hit["animation_type"])
                continue

            if midi_hit["type"] == "accent":
                start,end = 0, LED_COUNT
                hit_color = colours["accent_hit_1"]
            else:
                start, end = getStripSegmentIndex(midi_hit["note"])

            # Get colour
            drum_type = DRUMKIT_CONFIG[midi_hit["note"]["drum_type"]]
            hit_color = colours[drum_type]

            # Modify Brightness
            multiplier = midi_hit["velocity"] * ((100/127)) * 0.01
            pixel_color = [int(hit_color[0] * multiplier), int(hit_color[1] * multiplier),int(hit_color[2] * multiplier)]

            # Store colour
            for pixel in range(end-start):
                current_strip_values[pixel + start] = pixel_color

            # Set strip colour
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
