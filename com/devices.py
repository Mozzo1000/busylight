import serial.tools.list_ports

class Devices():
    def __init__(self):
        self.list = [
            p.device
            for p in serial.tools.list_ports.comports()
        ]