import socket
import struct

UDP_IP = "0.0.0.0"
UDP_PORT = 5606

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024 * 2) # buffer size is 1024 bytes
    #print ("Data:", data[0:18])
    version = struct.unpack('H', data[0:2])[0]
    print ("Build Version:", version)
    package = struct.unpack('B', data[2:3])[0]
    print ("Package Type:", (package & 0x3))
    print ("Sequence Number:", (package & 0xFC) << 2)
    g_state = struct.unpack('B', data[3:4])[0]
    print ("g_state:", g_state)
    n_part = struct.unpack('b', data[5:6])[0]
    print ("n_part:", n_part)
    speed = struct.unpack('f', data[120:124])[0]
    print ("speed:", speed)
    rpm = struct.unpack('H', data[124:126])[0]
    print ("rpm:", rpm)
