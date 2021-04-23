from ledStrip import *
from config import *

def powerUp():
    l = LedStrip(LED_COUNT)

    l.rainbow(20,100)