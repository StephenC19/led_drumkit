import mido
import time
import multiprocessing
from utils.utils import *
from utils.midiUtils import *
from config.config import *
from lib.ledStripDaemon import *

def listen_to_midi_notes():
    start_timer = True
    count = 0
    while start_timer:
        if read_json_file("active_control_file.json")["app_state"] == "start":
            break
        time.sleep(0.5)
        count += 1
        if count > 600:
            start_timer = False

    midi_connection = setup_custom_midi_connection(MIDI_UNIT)

    # Start LED control daemon with animation
    led_strip_message_queue = multiprocessing.Queue()
    led_strip_message_queue.put({"animation":True, "animation_type": 'startup'})
    led_strip_daemon_thread = multiprocessing.Process(target=ledStripDaemon, args=(led_strip_message_queue,))
    led_strip_daemon_thread.start()

    # Listen for midi messages
    for msg in midi_connection:
        if msg.type == "note_on":
            control_file = read_json_file("active_control_file.json")
            if control_file["animation"]:
                led_strip_message_queue.put({"animation":True, "animaton_type": control_file["animation_type"]})
                continue
            elif control_file["app_state"] == "stop":
                exit(1)

            if msg.note in PAD_NOTES or msg.note in CYMBAL_NOTES:
                led_strip_message_queue.put({"note":msg.note, "velocity":msg.velocity , "animation":False})

if __name__ == "__main__":
    listen_to_midi_notes()


#TODO
#remove animation once started
# - follow from main
# - remove start thing
# - add startup options in UI
# - build setup script
