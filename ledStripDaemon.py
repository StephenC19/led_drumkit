from ledStrip import *
from config import *
from hitAnimations import *
from ac import *
import time

# with open('./accentColors.json') as json_file:
#     print(json_file.read)
#     colors = json.load(json_file)

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

            if j["animation"]:
                for i in range(0, 100):
                    u = 100 - i
                    l.setSegment([u,u,u], 0, LED_COUNT)
                continue

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

            # Modify Brightness
            if int(j["velocity"]) > 80:
                mul = 1
            elif int(j["velocity"]) > 20:
                mul = j["velocity"]/80.0
            else:
                mul = 0.2
            hit_color = [int(hit_color[0]*mul), int(hit_color[1]*mul),int(hit_color[2]*mul)]


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
            print("Unexpected error:", sys.exc_info()[0])
            for i in range(len(led_values)):
                r = led_values[i][0]
                g = led_values[i][1]
                b = led_values[i][2]
                color = [g, r, b]
                l.setPixel(i, color)
                led_values[i] = linearFade(r, g, b)
            l.stripShow()