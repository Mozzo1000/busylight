import time
import board
import supervisor

import adafruit_dotstar

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

led.brightness = 0.5
device_info = {"device": "light", "version": "1.0"}

while True:
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        if value.startswith("s"):
            color = value.strip("s ")
            led[0] = int(color, 16)
            print(color)
        elif value.startswith("i"):
            print(device_info)
        elif value.startswith("p"):
            print("pong")
        elif value.startswith("b"):
            brightness = value.strip("b ")
            print(float(brightness))
            led.brightness = float(brightness)
            print(brightness)
        else:
            print("Unrecognizable command")
        