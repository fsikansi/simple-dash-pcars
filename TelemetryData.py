import struct

#Model class for Telemetry Packages
#Still a lot of data to read
class TelemetryData:
    def __init__(self, package):
        self.build_version = struct.unpack('H', package[0:2])[0]
        self.package_type = struct.unpack('B', package[2:3])[0] & 0x3
        self.sequence_number = (struct.unpack('B', package[2:3])[0] & 0xFC) << 2
        #Game states
        self.game_session_state = struct.unpack('B', package[3:4])[0]
        #Participant Info
        self.viewed_participant_index = struct.unpack('b', package[4:5])[0]
        self.num_participants = struct.unpack('b', package[5:6])[0]
        #Unfiltered input
        self.unfiltered_throttle = struct.unpack('B', package[6:7])[0]
        self.unfiltered_brake = struct.unpack('B', package[7:8])[0]
        self.unfiltered_steering = struct.unpack('b', package[8:9])[0]
        self.unfiltered_clutch = struct.unpack('B', package[9:10])[0]
        self.race_state_flags = struct.unpack('B', package[10:11])[0]
        #Event Information
        self.laps_in_event = struct.unpack('B', package[11:12])[0]
        #Timings
        self.best_lap_time = struct.unpack('f', package[12:16])[0]
        self.last_lap_time = struct.unpack('f', package[16:20])[0]
        self.current_time = struct.unpack('f', package[20:24])[0]
        self.split_time_ahead = struct.unpack('f', package[24:28])[0]
        self.split_time_behind = struct.unpack('f', package[28:32])[0]
        self.split_time = struct.unpack('f', package[32:36])[0]
        self.event_time_remaining = struct.unpack('f', package[36:40])[0]
        self.personal_fastest_lap_time = struct.unpack('f', package[40:44])[0]
        self.world_fastest_lap_time = struct.unpack('f', package[44:48])[0]
        self.current_sector1_time = struct.unpack('f', package[48:52])[0]
        self.current_sector2_time = struct.unpack('f', package[52:56])[0]
        self.current_sector3_time = struct.unpack('f', package[56:60])[0]
        self.fastest_sector1_time = struct.unpack('f', package[60:64])[0]
        self.fastest_sector2_time = struct.unpack('f', package[64:68])[0]
        self.fastest_sector3_time = struct.unpack('f', package[68:72])[0]
        self.personal_fastest_sector1_time = struct.unpack('f', package[72:76])[0]
        self.personal_fastest_sector2_time = struct.unpack('f', package[76:80])[0]
        self.personal_fastest_sector3_time = struct.unpack('f', package[80:84])[0]
        self.world_fastest_sector1_time = struct.unpack('f', package[84:88])[0]
        self.world_fastest_sector2_time = struct.unpack('f', package[88:92])[0]
        self.world_fastest_sector3_time = struct.unpack('f', package[92:96])[0]

        self.joy_pad = struct.unpack('H', package[96:98])[0]

        #Continue from here


        self.speed = struct.unpack('f', package[120:124])[0]
        self.rpm = struct.unpack('H', package[124:126])[0]
