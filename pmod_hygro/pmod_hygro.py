import time
from pmodhygro import PmodHygro

# Create i2c bus
sensor = PmodHygro()
sensor.begin_i2c()  # Forcer l'utilisation de I2C-2
print("Capteur initialisé avec succès !")

# Read data from Pmod HYGRO 
print("Attente 2 secondes pour stabilisation du capteur...")
time.sleep(2)
temp = sensor.get_temperature()
temp_f = sensor.get_temperature_f()
hum = sensor.get_humidity()

# Lire les valeurs obtenue
print(f"Température : {temp}°C")
print(f"Température (Fahrenheit) : {temp_f}°F")
print(f"Humidité : {hum}%")
