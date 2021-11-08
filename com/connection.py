import serial
import time

class Connection():
    def __init__(self, serial_port, baudrate):
        self.serial_port = serial_port
        self.baudrate = baudrate

        try:
            self.ser = serial.Serial(serial_port, baudrate)  # open serial port
        except:
            print("Error opening serial port")

    def send_command(self, command):
        command = command + b'\n\r'
        print(f"Sending Command: [{command}]")
        self.ser.write(command)
        return self._wait_for_reply(command)

    def _wait_for_reply(self, command):
        reply = b''

        for _ in range(len(command)):
            a = self.ser.read() # Read the loopback chars and ignore

        while True:
            a = self.ser.read()

            if a== b'\r':
                break

            else:
                reply += a

            time.sleep(0.01)

        print(f"Reply was: [{reply}]")
        self.ser.close()
        return reply
