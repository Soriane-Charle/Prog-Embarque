import smbus2
import time

bus = smbus2.SMBus(2)  # I2C-2
address = 0x37  # Adresse du capteur

# Envoyer un reset au capteur
bus.write_byte(address, 0x00)  # Commande reset
time.sleep(2)

# Lire une valeur de test
data = bus.read_byte(address)
print(f"Réponse après reset : {data}")
