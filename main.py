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

# Start reading MIDI messages
for msg in midi_connection:
    if msg.type == "note_on":
        if msg.note in ACTIVE_MIDI_PADS:
            print(msg)
            queue.put(msg.note)
