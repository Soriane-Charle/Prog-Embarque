import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

JA = [8, 10, 9, 11, 19, 21, 20, 18]
JB = [7, 10, 9, 11, 26, 13, 3, 2]
JC = [16, 14, 15, 17, 4, 12, 5, 6]

def gpio_set_direction(pin, direction):
    """ Configure la direction d'un GPIO (0 = entrée, 1 = sortie) """
    GPIO.setup(pin, GPIO.OUT if direction else GPIO.IN)

def gpio_set_value(pin, value):
    """ Écrit une valeur (0 ou 1) sur un GPIO en sortie """
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, value)

def gpio_get_value(pin):
    """ Lit l'état d'un GPIO en entrée (0 ou 1) """
    GPIO.setup(pin, GPIO.IN)  # Assure que le GPIO est bien en entrée
    return GPIO.input(pin)

