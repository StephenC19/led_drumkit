from main import *
from utils import *
from animations.kitAnimations import *
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

COLOUR_CONFIG_PATH = 'config/accentColors.json'
CONTROL_FILE_PATH = 'active_control_file.json'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/start_app": {"origins": "http://localhost:port"}})

@app.route('/start_app')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def start_app():
    data = read_json_file(CONTROL_FILE_PATH)
    data["app_state"] = 'start'
    write_json_file(CONTROL_FILE_PATH, data)
    return 'Powered on'


@app.route('/stop_app')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def stop_app():
    data = read_json_file(CONTROL_FILE_PATH)
    data["app_state"] = 'strop'
    write_json_file(CONTROL_FILE_PATH, data)
    return "Powered off"


@app.route('/change_color')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def change_color():
    color_type = request.args.get('color_type')
    red = int(request.args.get('red'))
    green = int(request.args.get('green'))
    blue = int(request.args.get('blue'))

    data = read_json_file(COLOUR_CONFIG_PATH)
    data[color_type] = [red, green, blue]
    write_json_file(COLOUR_CONFIG_PATH, data)
    return "Changed colour config"


@app.route('/add_animation')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def add_animation():
    data = read_json_file(CONTROL_FILE_PATH)
    data["animation"] = True
    data["animation_type"] = request.args.get('animation')
    write_json_file(COLOUR_CONFIG_PATH, data)
    return "Rainbow animation"

@app.route('/run_led_kit')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def run_led_kit():
    multiprocessing.Process(target=listen_to_midi_notes, args=()).start()
    return "Started led kit run"

@app.route('/midi_connections')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def midi_connections():
    return get_midi_connections()

@app.route('/turn_on_drum')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def turn_on_drum():
    turn_on_single_drum(request.args.get('drum_name'))
    return get_midi_connections()

@app.route('/add_new_config')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def midi_connections():
    config_name = request.args.get('config_name')
    if (valid_config_request(config_name)):
        write_json_file(config_name)


if __name__ == "__main__":
    if(len(sys.argv) > 0 and sys.argv[0] == "server_mode"):
        app.run(host='0.0.0.0')
    else:
        print("Running as standalone script with current config.\n To run in server mode run with 'server_mode'")
        listen_to_midi_notes()



#TODO
# - add feature of ambient strip sections
# - Design main page
# - create new config
# - edit config by lighting individual drums

# - remove animation once started
# - add startup options in UI
# - build setup script
