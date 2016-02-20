import TelemetryData
import ParticipantInfoStrings
import ParticipantInfoStringsAdditional
import struct
from UDPClient import UDPClient
import time
from ViewController import ViewTypes, ViewController

UDP_IP = "0.0.0.0"
UDP_PORT = 5606
running = True
#view_controller = ViewController(ViewTypes.CONSOLE)
view_controller = ViewController(ViewTypes.GPIO)

def check_package_type(package):
    return (struct.unpack('B', package[2:3])[0] & 0x3)

client = UDPClient(UDP_IP, UDP_PORT)

client.connect()
print("Connected to UDP stream")
while running:
    try:
        if client.last_package is not None:
            package_type = check_package_type(client.last_package)
            if (package_type == 0):
                telemetry_data = TelemetryData.TelemetryData(client.last_package)
                view_controller.update_telemetry(telemetry_data)
            elif (package_type == 1):
                participant_info = ParticipantInfoStrings.ParticipantInfoStrings(client.last_package)
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
                participant_info_additional = ParticipantInfoStringsAdditional.ParticipantInfoStringsAdditional(client.last_package)
                with open('participant_info_addition.txt', 'w') as p_add_info_file:
                    p_add_info_file.write('Participant Info Additional Strings\n')
                    p_add_info_file.write("Build Version:" + str(participant_info_additional.build_version) + "\n")
                    p_add_info_file.write("Names:\n")
                    for x in range(0,16):
                        p_add_info_file.write(participant_info_additional.name[x] + "\n")
        time.sleep(0.01)
    except KeyboardInterrupt:
        running = False
        client.close()
        print('Connection Closed')
