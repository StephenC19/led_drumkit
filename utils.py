def hex_rgb_converter(hex_value):
    value = hex_value.lstrip('#')
    lv = len(hex_value)
    return tuple(int(value[i:i+(int(lv/3))], 16) for i in range(0, lv, lv//3))

def rgb_converter(red, green, blue):
    color = [int(green), int(red), int(blue)]
    return color

def convert_brightness(brightness, red_value, green_value, blue_value):
    factor = float(brightness) / 10
    red = int(red_value*factor)
    green = int(green_value*factor)
    blue = int(blue_value*factor)
    return red, green, blue
