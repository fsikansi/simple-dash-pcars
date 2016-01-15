import TLV
import Convert
import struct

def create_tlv(telemetry_data):
    root_value = bytearray(create_lcd_tlv(telemetry_data).serialize()) + bytearray(create_led_tlv(telemetry_data).serialize()) + bytearray(create_seg7_tlv(telemetry_data).serialize())
    root = TLV.TLVNode(TLV.TAGList.ROOT, root_value)

    return root

def create_lcd_tlv(telemetry_data):
    return TLV.TLVNode(TLV.TAGList.LCD, (str(int(Convert.speed_to_kph(telemetry_data.speed))) + " kph").encode("ascii"))

def create_led_tlv(telemetry_data):
    return TLV.TLVNode(TLV.TAGList.LED, str(int((telemetry_data.rpm / telemetry_data.max_rpm) * 100)).encode('ascii'))

def create_seg7_tlv(telemetry_data):
    return TLV.TLVNode(TLV.TAGList.SEG7_1DIGIT, str(telemetry_data.current_gear).encode('ascii'))
