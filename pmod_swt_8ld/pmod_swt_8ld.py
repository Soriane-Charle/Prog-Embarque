import time
import sys
from gpio import JA, JC, JB, gpio_set_direction, gpio_set_value, gpio_get_value

# Configuration des GPIO
for i in range(8):  
    gpio_set_direction(JA[i], 0)  # Entrée pour les switches  
    gpio_set_direction(JC[i], 1)  # Sortie pour les LEDs  

try:
    while True:
        # Lire l'état des switches sur JA
        switch_states = [gpio_get_value(JA[i]) for i in range(4)]  # 🔥 Correction ici

        # Création du pattern pour contrôler les LEDs
        pattern = sum((1 << i) for i, state in enumerate(switch_states) if state)

        # Appliquer le pattern aux LEDs
        for i in range(4):
            gpio_set_value(JC[i], (pattern >> i) & 1)  

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Arrêt du programme.")

