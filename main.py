import mido
import json
import time
import multiprocessing
from config import *
from ledStripDaemon import *

def listen_to_midi_notes():

    while True:
        with open('control_file.txt') as f:
            if f.readline().rstrip() == "start":
                break
        time.sleep(0.5)

    # Open MIDI device connection
    try:
        midi_connection = mido.open_input(MIDI_UNIT)
    except:
        print("No MIDI device found. Please make sure a device is connected.")
        exit(1)

    # Start LED control daemon with animation
    queue = multiprocessing.Queue()
    queue.put({"animation":True, "animation_type": 'startup'})

    ld = multiprocessing.Process(target=ledStripDaemon, args=(queue,))
    ld.start()

    for msg in midi_connection:
        if msg.type == "note_on":

            # TODO: This is terrible. Just don't even read this block
            with open('control_file.txt') as f:
                if f.readline().rstrip() == "animation":
                    animation_type = f.readline().rstrip()
                    queue.put({"animation":True, "animaton_type": animation_type})
                    continue
                elif f.readline().rstrip() == "stop":
                    exit(1)
            # Did you actually read it? Don't judge me

            if msg.note in PADS_NOTES:
                print(msg)
                queue.put({"note":msg.note, "velocity":msg.velocity , "type":"pad", "animation":False})

            elif msg.note in CYMBAL_NOTES:
                queue.put({"note":msg.note, "velocity":msg.velocity , "type":"cymbal", "animation":False})

            elif msg.note == KICK_NOTE:
                queue.put({"note":msg.note, "velocity":msg.velocity , "type":"kick", "animation":False})


if __name__ == "__main__":
    # Start reading MIDI messages
    listen_to_midi_notes()
