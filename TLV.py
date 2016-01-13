#TLV class will be used to send data to Arduino using Serial Communication
class TLV:
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value
        self.lenght = len(value)
