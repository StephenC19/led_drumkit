from lib.ledStrip import *
from config.config import *

def powerUp():
    lStrip= LedStrip(LED_COUNT)

    lStrip.rainbow(20,100)
