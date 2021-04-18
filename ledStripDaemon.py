from ledStrip import *
from config import *
from animations import *

def getStartEnd(note):
    drum_name = MIDI_NOTE_INDEX[note]
    start = LED_DRUM_INDEX[drum_name][0]
    end = LED_DRUM_INDEX[drum_name][1]
    return start, end

def ledStripDaemon(queue):
    color = MAIN_COLOUR
    l = LedStrip(LED_COUNT)
    led_values = {}

    for i in range(LED_COUNT):
        led_values[i] = [0,0,0]

    while True:
        try:
            j = queue.get_nowait()
            start, end = getStartEnd(j)
            for k in range(end-start):
                #led_values[k+start] = [int(COLOURS[color]['g']),int(COLOURS[color]['r']),int(COLOURS[color]['b'])]
                led_values[k + start] = [0,0,255]

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