def linearFade(r, g, b, amount=5):
    mul = amount*2
    r = r - mul if r > 10 else 0
    g = g - mul if g > 10 else 0
    b = b - mul if b > 10 else 0

    return [r,g,b]


def logFade(r,g,b, power):
    if r > 5:
        mul = (r/260.0)**power
        r = int(mul * r)
    else:
        r = 0
    if g > 5:
        mul = (g/260.0)**power
        g = int(mul * g)
    else:
        g = 0
    if b > 5:
        mul = (b/260.0)**power
        b = int(mul * b)
    else:
        b = 0
    return [r,g,b]


def normalLogFade(r,g,b):
    return logFade(r, g, b, 2)


# def fadeToWhite():

# def strobe():

# def rainbowCircle():

# def spinAround():