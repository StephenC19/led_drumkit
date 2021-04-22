import mido
import json
import time
import multiprocessing
from config import *
from ledStripDaemon import *

# Start LED control daemon
queue = multiprocessing.Queue()
ld = multiprocessing.Process(target=ledStripDaemon, args=(queue,))
ld.start()

# Open MIDI device connection
try:
    midi_connection = mido.open_input(MIDI_UNIT)
except:
    print("No MIDI device found. Please make sure a device is connected.")
    exit(1)


def listen_to_midi_notes():
    for msg in midi_connection:
        if msg.type == "note_on":
            if msg.note in PADS_NOTES:
                print(msg)
                queue.put({"note":msg.note, "type":"pad"})

            elif msg.note in CYMBAL_NOTES:
                queue.put({"note":msg.note, "type":"cymbal"})

            elif msg.note == KICK_NOTE:
                queue.put({"note":msg.note, "type":"kick"})


if name == "__main__":
    # Start reading MIDI messages
    listen_to_midi_notes()
