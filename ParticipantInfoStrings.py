import struct

class ParticipantInfoStrings:

    def __init__(self, package):
        self.build_version = struct.unpack('H', package[0:2])[0]
        self.package_type = struct.unpack('B', package[2:3])[0] & 0x3
        self.sequence_number = (struct.unpack('B', package[2:3])[0] & 0xFC) << 2
        self.car_name = struct.unpack('s', package[3:131])[0]
        self.car_class_name = struct.unpack('s', package[131:195])[0]
        self.truck_location = struct.unpack('s', package[195:259])[0]
        self.truck_variation = struct.unpack('s', package[259:323])[0]
        i = 0
        ini_pos = 323
        while (i < 16):
            self.name[i] = struct.unpack('s', package[ini_pos:(ini_pos + 64)])[0]
            i += 1
            ini_pos += 64
