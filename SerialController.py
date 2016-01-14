import serial

class SerialController:
    def __init__(self):
        self.port = serial.Serial(
        	port='/dev/ttyUSB1',
        	baudrate=9600,
        	parity=serial.PARITY_ODD,
        	stopbits=serial.STOPBITS_TWO,
        	bytesize=serial.SEVENBITS
        )
        port.open()
        port.isOpen()

    def write(self, data):
        self.port.write(data)

    def close(self):
        self.port.close()
