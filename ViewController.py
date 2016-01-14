from enum import Enum
import os
import Convert
import ArduinoHelper
import SerialController

class ViewTypes(Enum):
    ARDUINO = 0
    CONSOLE = 1

class ViewController:
    def __init__(self, type):
        self.view_type = type
        self.serial = None
        if (type == ViewTypes.ARDUINO):
            self.serial = SerialController.SerialController()

    def update_telemetry(self, telemetry_data):
        if (self.view_type == ViewTypes.ARDUINO):
            tlv = ArduinoHelper.create_tlv(telemetry_data)
            #print("".join("%02x" % b for b in tlv.serialize()))
            self.serial.write(tlv.serialize())
        elif (self.view_type == ViewTypes.CONSOLE):
            os.system('cls' if os.name=='nt' else 'clear')
            print ("Build Version:", telemetry_data.build_version)
            print ("Package Type:", telemetry_data.package_type)
            print ("Sequence Number:", telemetry_data.sequence_number)
            print ("speed:", Convert.speed_to_kph(telemetry_data.speed))
            print ("RPM:", telemetry_data.rpm)
            print ("Gear:", telemetry_data.current_gear)
