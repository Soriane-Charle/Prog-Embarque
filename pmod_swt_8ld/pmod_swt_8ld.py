import time
import sys
from gpio import JA, JC, JB,  gpio_set_direction, gpio_get_value, gpio_set_value

# Configuration des GPIO
# - JA (Switches) en entrée
# - JC (LEDs) en sortie

for i in range(8):  
    gpio_set_direction(JA[i], 0)  # Entrée pour les switches  
    gpio_set_direction(JC[i], 1)  # Sortie pour les LEDs  

try:
    while True:
        # Lire l'état des switches sur JA
        switch_states = [gpio_get_value(JA[i]) for i in range(4)]
        
        # Création du pattern pour contrôler les LEDs
        pattern = sum((1 << i) for i, state in enumerate(switch_states) if state)

        # Allumage des LEDs sur JC selon le pattern
        for i in range(8):
            gpio_set_value(JC[i], 1 if pattern & (1 << i) else 0)

        time.sleep(0.5)  # Pause pour éviter une surcharge CPU

except KeyboardInterrupt:
    print("\nArrêt du programme...")

finally:
    # Extinction des LEDs avant de quitter
    for i in range(8):
        gpio_set_value(JC[i], 0)
    
    print("Ressources libérées.")

