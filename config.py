MIDI_UNIT = 'TD-17:TD-17 MIDI 1 20:0'

STRIP_GPIO_PIN = 18

LED_COUNT = 600

PADS_NOTES = [38,48,45,43,27,40,50]

CYMBAL_NOTES = [49,55,52,57,51,53,59,26,22,44]

KICK_NOTE = 36

SNARE_NOTE = 38

ACCENT_NOTE_1 = 47

ACCENT_NOTE_2 = 58

MIDI_NOTE_INDEX = {
    36 : "kick",
    38 : "snare",
    40 : "snare",
    48 : "tom1",
    50 : "tom1",
    45 : "tom2",
    47 : "tom2",
    43 : "tom3",
    58 : "tom3",
    27 : "tom4",
    49 : "crash1",
    55 : "crash1",
    52 : "crash2",
    57 : "crash2",
    51 : "ride",
    53 : "ride",
    59 : "ride",
    26 : "hihat",
    22 : "hihat",
    44 : "hihat"
}

LED_DRUM_INDEX = {
    "kick":[0, 300],
    "snare": [300, 355],
    "tom1":[355, 387],
    "tom2":[387, 420],
    "tom3":[420, 453],
    "tom4":[453, 507],
    "hihat":[573,597],
    "crash1":[551, 573],
    "crash2":[529,551],
    "ride":[507, 529]
}

COLOURS = {
    "red": {
        "r": 255,
        "g": 0,
        "b": 0
    },
    "green": {
        "r": 0,
        "g": 255,
        "b": 0
    },
    "blue": {
        "r": 0,
        "g": 0,
        "b": 255
    },
    "purple": {
        "r": 200,
        "g": 0,
        "b": 200
    },
    "orange": {
        "r": 200,
        "g": 0,
        "b": 200
    },
    "yellow": {
        "r": 200,
        "g": 0,
        "b": 200
    },
    "cyan": {
        "r": 200,
        "g": 0,
        "b": 200
    }
}