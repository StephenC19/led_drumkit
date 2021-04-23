import multiprocessing
from main import *
from kitAnimations import *
from flask import Flask
app = Flask(__name__)


# LED drums process
p = multiprocessing.Process(target=listen_to_midi_notes())

@app.route('/start_app')
def hello_world():
    powerUp()
    p.start()
    return 'Hello, World!'

# @app.route('/change_accent_color')
# def change_accent_color():
#     color_type = int(request.args.get('color_type'))
#     red = int(request.args.get('red'))
#     green = int(request.args.get('green'))
#     blue = int(request.args.get('blue'))

#     with open('accentColors.json', 'w') as outfile:
#         data = json.load(json_file)
#         data[color_type] = [red, green, blue]
#         json.dump(data, outfile)

#     return "Successfully changed to the new color"

@app.route('/stop_app')
def power_down():
    # Stop the main thread and gpio cleanup
    # Run power down animation
    p.stop()
    return "Powered off"

if __name__ == "__main__":
    app.run()
