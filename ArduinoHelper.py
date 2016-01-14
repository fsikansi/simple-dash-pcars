import TLV
import Convert
import struct

def create_tlv(telemetry_data):
    lcd = TLV.TLVNode(TLV.TAGList.LCD, (str(int(Convert.speed_to_kph(telemetry_data.speed))) + " kph").encode("ascii"))
    led = TLV.TLVNode(TLV.TAGList.LED, str(int((telemetry_data.rpm / telemetry_data.max_rpm) * 100)).encode('ascii'))
    seg7 = TLV.TLVNode(TLV.TAGList.SEG7_1DIGIT, str(telemetry_data.current_gear).encode('ascii'))

    root_value = bytearray(lcd.serialize()) + bytearray(led.serialize()) + bytearray(seg7.serialize())
    root = TLV.TLVNode(TLV.TAGList.ROOT, root_value)

    return root
