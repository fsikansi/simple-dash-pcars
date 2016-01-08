import socket
import TelemetryData
import Convert

def check_package_type(package) {
    return (struct.unpack('B', package[2:3])[0] & 0x3)
}

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
        pass
    elif (package_type == 2):
        pass 
    print ("Build Version:", telemetry_data.build_version)
    print ("Package Type:", telemetry_data.package_type)
    print ("Sequence Number:", telemetry_data.sequence_number)
    print ("speed:", Convert.speed_to_kph(telemetry_data.speed))
    print ("rpm:", telemetry_data.rpm)
