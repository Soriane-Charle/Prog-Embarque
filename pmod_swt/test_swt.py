import RPi.GPIO as GPIO
import time

# Définir les numéros de GPIO pour les 4 interrupteurs
SWITCH_PINS = [8, 10, 9, 11, 26, 13, 3, 2]
LED_PINS = [16, 14, 15, 17, 4, 12, 5, 6]

# Initialisation de GPIO
GPIO.setmode(GPIO.BCM)
for pin in SWITCH_PINS:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
# Configurer les interrupteurs comme entrées avec résistance pull-down
for pin in SWITCH_PINS:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Configurer les LED comme sorties
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        # Lire l'état des interrupteurs
        switch_states = [GPIO.input(pin) for pin in SWITCH_PINS]
        
        # Allumer/éteindre les LED en fonction des interrupteurs
        for i, state in enumerate(switch_states):
            if state == 1:  # Si l'interrupteur est pressé (état HIGH)
                GPIO.output(LED_PINS[i], GPIO.HIGH)  # Allumer la LED correspondante
            else:
                GPIO.output(LED_PINS[i], GPIO.LOW)  # Éteindre la LED correspondante

        # Afficher l'état des interrupteurs et des LED
        print("État des interrupteurs : ", switch_states)
        print("LEDs allumées : ", [GPIO.input(pin) for pin in LED_PINS])
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Arrêt du programme.")

finally:
    GPIO.cleanup() 
