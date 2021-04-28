import multiprocessing
from main import *
from kitAnimations import *
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/start_app": {"origins": "http://localhost:port"}})

@app.route('/start_app')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def start_app():
    with open('control_file.txt', 'w') as f:
        f.write('start')
    return 'Hello, World!'

@app.route('/stop_app')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def stop_app():
    with open('control_file.txt', 'w') as f:
        f.write('stop')
    return "Powered off"

@app.route('/change_color')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def change_color():
    color_type = request.args.get('color_type')
    red = int(request.args.get('red'))
    green = int(request.args.get('green'))
    blue = int(request.args.get('blue'))

    with open('accentColors.json') as json_file:
        data = json.load(json_file)
        data[color_type] = [red, green, blue]
    with open('accentColors.json', 'w') as outfile:
        json.dump(data, outfile, indent = 4)
    return "Successfully changed to the new color"

@app.route('/add_animation')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def add_animation():
    animation = request.args.get('animation')
    with open('control_file.txt', 'w') as f:
        f.write("animation\n" + animation)
    return "Rainbow animation"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
