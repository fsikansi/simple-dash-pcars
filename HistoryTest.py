import TelemetryData
from ViewController import ViewTypes, ViewController
import pickle
import struct
import time

def check_package_type(package):
    return (struct.unpack('B', package[2:3])[0] & 0x3)

view_controller = ViewController(ViewTypes.GPIO)
#view_controller = ViewController(ViewTypes.ARDUINO)

with open("history.dat", "rb") as input:
    history = pickle.load(input)
    i = 0;
    for data in history:
        package_type = check_package_type(data)
        if (package_type == 0):
            telemetry_data = TelemetryData.TelemetryData(data)
            view_controller.update_telemetry(telemetry_data)
        time.sleep(0.016)
