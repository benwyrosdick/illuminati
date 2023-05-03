# Setup NeoPixel on your Pi

Find official documentation here: https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage

On a Raspberry Pi, open a terminal and enter the following commands:

    sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel pyyaml
    sudo python3 -m pip install --force-reinstall adafruit-blinka

# Setup Illuminati to control the LEDs

On a Raspberry Pi, open a terminal and enter the following commands:

    cd /opt
    sudo mkdir illuminati
    sudo chown $USER: illuminati
    git clone https://github.com/benwyrosdick/illuminati.git illuminati

Then to have it start automatically run the following:

    sudo cp /opt/illuminati/illuminati.service /etc/systemd/system/
    sudo chown root:root /etc/systemd/system/illuminati.service
    sudo chmod 644 /etc/systemd/system/illuminati.service

Enable using:

    sudo systemctl start illuminati.service
    sudo systemctl enable illuminati.service