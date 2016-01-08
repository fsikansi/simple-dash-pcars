import struct

class ParticipantInfo:

    def __init__(self, package):
        self.world_position[0] = struct.unpack('h', package[0:2])[0]
        self.world_position[1] = struct.unpack('h', package[2:4])[0]
        self.world_position[2] = struct.unpack('h', package[4:6])[0]
        self.current_lap_distance = struct.unpack('H', package[6:8])[0]
        self.race_position = struct.unpack('B', package[8:9])[0]
        self.laps_completed = struct.unpack('B', package[9:10])[0]
        self.current_lap = struct.unpack('B', package[10:11])[0]
        self.sector = struct.unpack('B', package[11:12])[0]
        self.last_sector_time = struct.unpack('f', package[12:16])[0]
