class LightCommands():
    def __init__(self):
        pass

    def set_color(self, hex):
        return b's ' + hex

    def info(self):
        return b'i'

    def ping(self):
        return b'p'
    
    def set_brightness(self, level):
        return b'b ' + level