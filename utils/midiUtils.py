import mido

def setup_midi_connection():
    device_list = mido.get_input_names()
    device_choice = input("Select the midi device by inputting the number choice:\n" + str(device_list))
    midi_device = device_list[int(device_choice) - 1]

    # Open MIDI device connection
    try:
        return mido.open_input(midi_device)
    except:
        print("No MIDI device found. Please make sure a device is connected.")
        exit(1)

def setup_custom_midi_connection(midi_device):
    device_list = mido.get_input_names()
    for device in device_list:
        if device == midi_device:
            return mido.open_input(midi_device)

    print("No MIDI device found. Please make sure a device is connected.")
    exit(1)

def get_midi_connections():
    return mido.get_input_names()
