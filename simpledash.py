import socket
import TelemetryData
import ParticipantInfoStrings
import ParticipantInfoStringsAdditional
import struct
import Convert
import os

def check_package_type(package):
    return (struct.unpack('B', package[2:3])[0] & 0x3)

UDP_IP = "0.0.0.0"
UDP_PORT = 5606

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024 * 2) # buffer size is 1024 bytes
    package_type = check_package_type(data)
    if (package_type == 0):
        telemetry_data = TelemetryData.TelemetryData(data)
    elif (package_type == 1):
        participant_info = ParticipantInfoStrings.ParticipantInfoStrings(data)
        with open('participant_info.txt', 'w') as p_info_file:
            p_info_file.write('Participant Info Strings\n')
            p_info_file.write("Build Version:" + str(participant_info.build_version) + "\n")
            p_info_file.write("Car Name:" + participant_info.car_name + "\n")
            p_info_file.write("Car Class:" + participant_info.car_class_name + "\n")
            p_info_file.write("Track Location:" + participant_info.truck_location + "\n")
            p_info_file.write("Track Variation:" + participant_info.truck_variation + "\n")
            p_info_file.write("Names:\n")
            for x in range(0,16):
                p_info_file.write(participant_info.name[x] + "\n")
    elif (package_type == 2):
        participant_info_additional = ParticipantInfoStringsAdditional.ParticipantInfoStringsAdditional(data)
        with open('participant_info_addition.txt', 'w') as p_add_info_file:
            p_add_info_file.write('Participant Info Additional Strings\n')
            p_add_info_file.write("Build Version:" + str(participant_info_additional.build_version) + "\n")
            p_add_info_file.write("Names:\n")
            for x in range(0,16):
                p_add_info_file.write(participant_info_additional.name[x] + "\n")
    os.system('cls' if os.name=='nt' else 'clear')
    print ("Build Version:", telemetry_data.build_version)
    print ("Package Type:", telemetry_data.package_type)
    print ("Sequence Number:", telemetry_data.sequence_number)
    print ("speed:", Convert.speed_to_kph(telemetry_data.speed))
    print ("RPM:", telemetry_data.rpm)
    print ("Gear:", telemetry_data.current_gear)
