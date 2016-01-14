from enum import Enum
import struct
#TLV class will be used to send data to Arduino using Serial Communication
class TLVNode:
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value
        self.lenght = len(value)

    def serialize(self):
        return bytearray(self.tag.value) + struct.pack("H", self.lenght) + bytearray(self.value)

class TAGList(Enum):
    ROOT = [0xDF, 0x00]
    LCD = [0xDF, 0x01]
    LED = [0xDF, 0x02]
    SEG7_1DIGIT = [0xDF, 0x03]
    SEG7_4DIGIT = [0xDF, 0x04]
