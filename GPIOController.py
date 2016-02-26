import RPi.GPIO as GPIO
import Adafruit_CharLCD

class GPIOController:

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
    LCD_RS = 4
    LCD_EN = 10
    LCD_DATA_1 = 19
    LCD_DATA_2 = 26
    LCD_DATA_3 = 24
    LCD_DATA_4 = 12

    numbers = {
        0:(0,0,0,0,0,0,1),
        1:(1,0,0,1,1,1,1),
        2:(0,0,1,0,0,1,0),
        3:(0,0,0,0,1,1,0),
        4:(1,0,0,1,1,0,0),
        5:(0,1,0,0,1,0,0),
        6:(0,1,0,0,0,0,0),
        7:(0,0,0,1,1,1,1),
        8:(0,0,0,0,0,0,0),
        9:(0,0,0,0,1,0,0)}

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        #self.configure_leds()
        self.configure_7_segments()
        self.configure_lcd()
        self.lcd = None

    def configure_leds(self):
        GPIO.setup(RPM_1_LEVEL,GPIO.OUT)
        GPIO.setup(RPM_2_LEVEL,GPIO.OUT)
        GPIO.setup(RPM_3_LEVEL,GPIO.OUT)
        GPIO.setup(RPM_4_LEVEL,GPIO.OUT)
        GPIO.setup(RPM_5_LEVEL,GPIO.OUT)

    def configure_7_segments(self):
        GPIO.setup(self.SEG7_A,GPIO.OUT, initial=1)
        GPIO.setup(self.SEG7_B,GPIO.OUT, initial=1)
        GPIO.setup(self.SEG7_C,GPIO.OUT, initial=1)
        GPIO.setup(self.SEG7_D,GPIO.OUT, initial=1)
        GPIO.setup(self.SEG7_E,GPIO.OUT, initial=1)
        GPIO.setup(self.SEG7_F,GPIO.OUT, initial=1)
        GPIO.setup(self.SEG7_G,GPIO.OUT, initial=1)

    def configure_lcd(self):
        self.lcd = Adafruit_CharLCD(LCD_RS, LCD_EN, [LCD_DATA_1, LCD_DATA_2, LCD_DATA_3, LCD_DATA_4])


    def update_leds(self, telemetry_data):
        rpm_percentage = int((telemetry_data.rpm / telemetry_data.max_rpm) * 100)
        if (rpm_percentage > 95):
            GPIO.output(self.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_2_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_3_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_4_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_5_LEVEL,GPIO.HIGH)
        elif (rpm_percentage > 91):
            GPIO.output(self.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_2_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_3_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_4_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_5_LEVEL,GPIO.LOW)
        elif (rpm_percentage > 87):
            GPIO.output(self.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_2_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_3_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_4_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_5_LEVEL,GPIO.LOW)
        elif (rpm_percentage > 84):
            GPIO.output(self.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_2_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_3_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_4_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_5_LEVEL,GPIO.LOW)
        elif (rpm_percentage > 80):
            GPIO.output(self.RPM_1_LEVEL,GPIO.HIGH)
            GPIO.output(self.RPM_2_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_3_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_4_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_5_LEVEL,GPIO.LOW)
        else:
            GPIO.output(self.RPM_1_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_2_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_3_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_4_LEVEL,GPIO.LOW)
            GPIO.output(self.RPM_5_LEVEL,GPIO.LOW)

    def update_7_segments(self, telemetry_data):
        if (telemetry_data.current_gear < 10):
            GPIO.output(self.SEG7_A, self.numbers[telemetry_data.current_gear][0])
            GPIO.output(self.SEG7_B, self.numbers[telemetry_data.current_gear][1])
            GPIO.output(self.SEG7_C, self.numbers[telemetry_data.current_gear][2])
            GPIO.output(self.SEG7_D, self.numbers[telemetry_data.current_gear][3])
            GPIO.output(self.SEG7_E, self.numbers[telemetry_data.current_gear][4])
            GPIO.output(self.SEG7_F, self.numbers[telemetry_data.current_gear][5])
            GPIO.output(self.SEG7_G, self.numbers[telemetry_data.current_gear][6])

    def update_lcd(self, telemetry_data):
        self.lcd.clear()
        self.lcd.message(str(int(Convert.speed_to_kph(telemetry_data.speed))) + " KPH")


    def update_all(self, telemetry_data):
        self.update_7_segments(telemetry_data)
        self.update_leds(telemetry_data)
        self.update_lcd(telemetry_data)
