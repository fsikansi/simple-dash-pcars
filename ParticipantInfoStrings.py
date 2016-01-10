import struct

class ParticipantInfoStrings:

    def __init__(self, package):
        self.build_version = struct.unpack('H', package[0:2])[0]
        self.package_type = struct.unpack('B', package[2:3])[0] & 0x3
        self.sequence_number = (struct.unpack('B', package[2:3])[0] & 0xFC) << 2
        self.car_name = struct.unpack('<64s', package[3:67])[0].decode("ISO-8859-1")
        self.car_class_name = struct.unpack('<64s', package[67:131])[0].decode("ISO-8859-1")
        self.truck_location = struct.unpack('<64s', package[131:195])[0].decode("ISO-8859-1")
        self.truck_variation = struct.unpack('<64s', package[195:259])[0].decode("ISO-8859-1")
        self.name = []
        i = 0
        ini_pos = 259
        while (i < 16):
            self.name.append(struct.unpack('<64s', package[ini_pos:(ini_pos + 64)])[0].decode("ISO-8859-1"))
            i += 1
            ini_pos += 64
