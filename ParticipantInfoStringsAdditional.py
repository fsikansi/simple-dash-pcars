import struct

class ParticipantInfoStringsAdditional:

    def __init__(self, package):
        self.build_version = struct.unpack('H', package[0:2])[0]
        self.package_type = struct.unpack('B', package[2:3])[0] & 0x3
        self.sequence_number = (struct.unpack('B', package[2:3])[0] & 0xFC) << 2
        self.offset = struct.unpack('B', package[3:4])[0]
        i = 0
        ini_pos = 4
        while (i < 16):
            self.name[i] = struct.unpack('s', package[ini_pos:(ini_pos + 64)])[0]
            i += 1
            ini_pos += 64
