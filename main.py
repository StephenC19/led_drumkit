from config.config import *
import mido
import json
import time
import multiprocessing
from ledStripDaemon import *
from midiUtils import *

def read_control_file():
    with open('active_control_file.json') as json_file:
        return json.load(json_file)

def listen_to_midi_notes():
    while True:
        if read_control_file["app_state"] == "start":
            break
        time.sleep(0.5)
    midi_connection = setup_custom_midi_connection(MIDI_UNIT)

    # Start LED control daemon with animation
    led_strip_message_queue = multiprocessing.Queue()
    led_strip_message_queue.put({"animation":True, "animation_type": 'startup'})
    led_strip_daemon_thread = multiprocessing.Process(target=ledStripDaemon, args=(led_strip_message_queue,))
    led_strip_daemon_thread.start()

    # Listen for midi messages
    for msg in midi_connection:
        if msg.type == "note_on":
            control_file = read_control_file
            if control_file["animation"]:
                led_strip_message_queue.put({"animation":True, "animaton_type": control_file["animation_type"]})
                continue
            elif control_file["app_state"] == "stop":
                exit(1)

            if msg.note in PAD_NOTES or msg.note in CYMBAL_NOTES:
                led_strip_message_queue.put({"note":msg.note, "velocity":msg.velocity , "animation":False})

            #TODO remove
            # if msg.note == SNARE_NOTE:
            #     led_strip_message_queue.put({"note":msg.note, "velocity":msg.velocity , "type":"snare", "animation":False})
            # elif msg.note == KICK_NOTE:
            #     led_strip_message_queue.put({"note":msg.note, "velocity":msg.velocity , "type":"kick", "animation":False})
            # elif msg.note in PADS_NOTES:
            #     led_strip_message_queue.put({"note":msg.note, "velocity":msg.velocity , "type":"pad", "animation":False})
            # elif msg.note in CYMBAL_NOTES:
            #     led_strip_message_queue.put({"note":msg.note, "velocity":msg.velocity , "type":"cymbal", "animation":False})
            # elif msg.note == ACCENT_NOTE_1:
            #     led_strip_message_queue.put({"note":msg.note, "velocity":msg.velocity , "type":"accent_1", "animation":False})
            # elif msg.note == ACCENT_NOTE_2:
            #     led_strip_message_queue.put({"note":msg.note, "velocity":msg.velocity , "type":"accent_2", "animation":False})

if __name__ == "__main__":
    # Start reading MIDI messages
    listen_to_midi_notes()




#TODO
# - rebuild from config
# - follow from main
# - remove start thing
# - add startup options in UI
# - build setup script
