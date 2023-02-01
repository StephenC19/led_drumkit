# led_drumkit
###### By Stephen Colfer

## Description
Turn your drumkit into a light show! By mounting an led strip to your drums you can use this code to control the strip through MIDI. With the correct setup the LEDs will react to the midi drum pads. This repo also includes the code for an optional web app to control the LED colours. Follow the steps here in the README for materials and setup. For more info on the project check out the video: https://youtu.be/ctKZRcTf2wk


## Materials
- Raspberry Pi
- [WS2812 RGB LED Strip](https://www.amazon.co.uk/CHINLY-WS2812B-Individually-Addressable-Waterproof/dp/B01LSF4Q0A?pd_rd_w=Y8qio&pf_rd_p=907ba819-1a37-4335-8b84-d82a78945ade&pf_rd_r=XJJKR5NCNPWB7S3EAEC3&pd_rd_r=6c6d6a0f-9829-4747-8fee-2d0778cb1b8d&pd_rd_wg=QvtLt&pd_rd_i=B01LSF4Q0A&psc=1&ref_=pd_bap_d_rp_2_t) (or similar strip with indivually addresable LEDs)
- [Power supply suitedable](https://www.amazon.co.uk/gp/product/B07C4SNYCH/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) for the LED strip. 10A per 300 5v leds in this case.
- Drum kit capable of MIDI note output (electric drumkit or acoustic with triggers)
- (Optional) [Aluminium LED channel](https://www.amazon.co.uk/Chesbung-Aluminum-Channels-Diffusers-Mounting/dp/B07RJVV9MY?pd_rd_w=TNSWg&pf_rd_p=508c5101-ccd9-46e7-b139-f5fa5b359865&pf_rd_r=BYKFHRAD8NJNQ7T5TBR3&pd_rd_r=4dde0c46-0170-4a38-af65-c321c9e4feb1&pd_rd_wg=nqF4R&psc=1&ref_=pd_bap_d_csi_vtp_0_t) for mounting to stands.
- (Optional) [Useful power connectors](https://www.amazon.co.uk/gp/product/B01JZ3O36O/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- (Optional) [No solder strip connectors](https://www.amazon.co.uk/gp/product/B08FHXW4G5/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)


## Installation

### LED setup

Using the steps listed here you can setup you Raspberry pi to control an LED strip. These steps are based off the info [here](https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/)

1. Install packages on the Raspberry Pi. `pip install requirements.txt`, `sudo pip install rpi_ws281x`
2. Connect the Power supply to the strip and link to the Pi
    - Connect the data line (green) to pin 18 in case
    - Connect the ground (black) to pin 6 or any available ground pin.
    - Connect the other parts of the led to the power supply.
3. Run the example script from the link above `examples/strandtest.py`
4. Connect the midi unit to the Pi (through USB). You can test the connection by running the following in python
```python
import mido

mido.get_input_names() # Get connected midi device names

with mido.open_input('<midi_device_name>') as inport:
    for message in inport:
        print(message)
```
5. Cut the LED strip and mount each section to your drumkit
6. Modify `config.py` to set the length of the LED strips (TODO: add a test script to handle this)
7. Modify `accentColors.json` to choose the LED colours.
7. Run the main script and enjoy your led light show! `python main.py`

### Web app control setup
1. Install npm
2. Install vue js `npm install vue`
3. `cd UI/` and run `npm update`
4. Replace the ip in `src/components/var.js` to the ip of the raspberry pi (TODO: Add a script to handle this)
5. Start the server `npm run serve`
6. Start the control server `python controlServer.py`
7. Open the http://<ip>:8080/ and enjoy!

### Pi Setup
1. Make sure it's up to date
`sudo apt-get update`
2. Install required packages
`sudo apt-get install gcc make build-essential python-dev git scons swig`
3. Deactive the audio output
sudo echo "blacklist snd_bcm2835" > /etc/modprobe.d/snd-blacklist.conf
4.
5. Restart
`sudo reboot`
6. Download the LED control library
`git clone https://github.com/jgarff/rpi_ws281x`
7. Compile the libraries
`cd rpi_ws281x/;sudo scons`
8. Setup python libraries
```
cd python
sudo python3 setup.py build
sudo python3 setup.py install
sudo pip3 install adafruit-circuitpython-neopixel
```
9. Setup test script
`sudo nano examples/strandtest.py`
Then modifiy the constants in the class like the LED_PIN and LED_COUNT
10. Run the code
`sudo python3 examples/strandtest.py`


### Drum Installation

This will vary depending on the drumkit. Most led strips come with small clips that can be stuck or screwed into the drum.
This can be avoided by using some for of tape or even covering part of the drum wall with tape and then using a glue gun
to gule the strip to the part of the drum with tape. This makes it easy to take the strip off the drums if needed with no
damage.

The strip will also need to be cut and either clipped together using something like this TODO or soldering together for
better secure line connections.


### Server Start
