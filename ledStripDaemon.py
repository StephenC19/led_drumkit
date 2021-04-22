from ledStrip import *
from config import *
from animations import *

with open('accentColors.json', 'w') as outfile:
    colors = json.load(json_file)

def getStartEnd(note):
    drum_name = MIDI_NOTE_INDEX[note]
    start = LED_DRUM_INDEX[drum_name][0]
    end = LED_DRUM_INDEX[drum_name][1]
    return start, end

def ledStripDaemon(queue):
    l = LedStrip(LED_COUNT)
    led_values = {}

    for i in range(LED_COUNT):
        led_values[i] = [0,0,0]

    while True:
        try:
            j = queue.get_nowait()
            if j["type"] == "accent":
                start,end = 0, LED_COUNT
                hit_color = colors["accent_hit_1_color"]
            else:
                start, end = getStartEnd(j["note"])

            # Set Color
            if j["type"] == "kick":
                hit_color = colors["kick_color"]
            elif j["type"] == "pad":
                hit_color = colors["pad_color"]
            elif j["type"] == "cymbal":
                hit_color = colors["cymbal_color"]


            for k in range(end-start):
                led_values[k + start] = hit_color

            for i in range(len(led_values)):
                r = led_values[i][0]
                g = led_values[i][1]
                b = led_values[i][2]
                color = [g, r, b]
                l.setPixel(i, color)
                led_values[i] = linearFade(r, g, b)
            l.stripShow()
        except:
            for i in range(len(led_values)):
                r = led_values[i][0]
                g = led_values[i][1]
                b = led_values[i][2]
                color = [g, r, b]
                l.setPixel(i, color)
                led_values[i] = linearFade(r, g, b)
            l.stripShow()