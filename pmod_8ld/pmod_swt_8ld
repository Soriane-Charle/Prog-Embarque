import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


JA = [8, 10, 9, 11, 19, 21, 20, 18]
JB = [7, 10, 9, 11, 26, 13, 3, 2]
JC = [16, 14, 15, 17, 4, 12, 5, 6]

def gpio_set_direction(pin, direction):
    GPIO.setup(pin, GPIO.OUT if direction else GPIO.IN)

def gpio_set_value(pin, value):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, value)
 

