from com.connection import Connection
from com.commands import LightCommands

conn = Connection('/dev/tty.usbmodem14101', 115200)
#conn.send_command(LightCommands().set_color(b'0xeb343a'))
#json_2 = json.decode('utf8').replace("'", '"')
#print(json_2)