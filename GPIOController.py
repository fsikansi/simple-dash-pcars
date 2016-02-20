import RPi.GPIO as GPIO

class InputTypes(Enum):
    RPM_1_LEVEL = 17
    RPM_2_LEVEL = 18
    RPM_3_LEVEL = 27
    RPM_4_LEVEL = 22
    RPM_5_LEVEL = 23
    SEG7_A = 16
    SEG7_B = 25
    SEG7_C = 5
    SEG7_D = 6
    SEG7_E = 13
    SEG7_F = 21
    SEG7_G = 20

class GPIOController:

    numbers = {
        0:(1,1,1,1,1,1,0),
        1:(0,1,1,0,0,0,0),
        2:(1,1,0,1,1,0,1),
        3:(1,1,1,1,0,0,1),
        4:(0,1,1,0,0,1,1),
        5:(1,0,1,1,0,1,1),
        6:(1,0,1,1,1,1,1),
        7:(1,1,1,0,0,0,0),
        8:(1,1,1,1,1,1,1),
        9:(1,1,1,1,0,1,1)}

    segments = [InputTypes.SEG7_A, InputTypes.SEG7_B, InputTypes.SEG7_C, InputTypes.SEG7_D, InputTypes.SEG7_E, InputTypes.SEG7_F, InputTypes.SEG7_G]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        #configure_leds()
        configure_7_segments()

    def configure_leds():
        GPIO.setup(InputTypes.RPM_1_LEVEL,GPIO.OUT)
        GPIO.setup(InputTypes.RPM_2_LEVEL,GPIO.OUT)
        GPIO.setup(InputTypes.RPM_3_LEVEL,GPIO.OUT)
        GPIO.setup(InputTypes.RPM_4_LEVEL,GPIO.OUT)
        GPIO.setup(InputTypes.RPM_5_LEVEL,GPIO.OUT)

    def configure_7_segments():
        GPIO.setup(InputTypes.SEG7_A,GPIO.OUT)
        GPIO.setup(InputTypes.SEG7_B,GPIO.OUT)
        GPIO.setup(InputTypes.SEG7_C,GPIO.OUT)
        GPIO.setup(InputTypes.SEG7_D,GPIO.OUT)
        GPIO.setup(InputTypes.SEG7_E,GPIO.OUT)
        GPIO.setup(InputTypes.SEG7_F,GPIO.OUT)
        GPIO.setup(InputTypes.SEG7_G,GPIO.OUT)

    def update_leds(telemetry_data):
        rpm_percentage = int((telemetry_data.rpm / telemetry_data.max_rpm) * 100)
        if (rpm_percentage > 95):
            GPIO.output(InputTypes.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_2_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_3_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_4_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_5_LEVEL,GPIO.HIGH)
        elif (rpm_percentage > 91):
            GPIO.output(InputTypes.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_2_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_3_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_4_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_5_LEVEL,GPIO.LOW)
        elif (rpm_percentage > 87):
            GPIO.output(InputTypes.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_2_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_3_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_4_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_5_LEVEL,GPIO.LOW)
        elif (rpm_percentage > 84):
            GPIO.output(InputTypes.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_2_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_3_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_4_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_5_LEVEL,GPIO.LOW)
        elif (rpm_percentage > 80):
            GPIO.output(InputTypes.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(InputTypes.RPM_2_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_3_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_4_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_5_LEVEL,GPIO.LOW)
        else:
            GPIO.output(InputTypes.RPM_1_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_2_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_3_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_4_LEVEL,GPIO.LOW)
            GPIO.output(InputTypes.RPM_5_LEVEL,GPIO.LOW)

    def update_7_segments(telemetry_data):
        if (telemetry_data.current_gear < 10):
            GPIO.output(segments, numbers(telemetry_data.current_gear))

    def update_all(telemetry_data):
        update_7_segments(telemetry_data)
        #update_leds(telemetry_data)
