def linearFade(r, g, b):
    r = r - 10 if r > 10 else 0
    g = g - 10 if g > 10 else 0
    b = b - 10 if b > 10 else 0

    return [r,g,b]


def logFade(r,g,b, power):
    if r > 10:
        r = ((r/260)**power) * r
    else:
        r = 0
    if g > 10:
        g = ((g/260)**power) * g
    else:
        g = 0
    if b > 10:
        b = ((b/260)**power) * b
    else:
        b = 0

    return [r,g,b]


def normalLogFade(r,g,b):
    return logFade(r, g, b, 2)


# def fadeToWhite():

# def strobe():

# def rainbowCircle():

# def spinAround():