from sense_hat import SenseHat

# Initialisation de l'objet SenseHat
sense = SenseHat()

# Récupérer les valeurs des capteurs
temperature = sense.get_temperature()  # Température en Celsius
humidity = sense.get_humidity()       # Humidité relative en %
pressure = sense.get_pressure()       # Pression atmosphérique en hPa

# Fonction pour définir la couleur en fonction de la température
def get_temperature_color(temp):
    if temp < 20:
        return (0, 0, 255)  # Bleu pour une température inférieure à 20°C
    elif temp < 30:
        return (0, 255, 0)  # Vert pour une température entre 20°C et 30°C
    else:
        return (255, 0, 0)  # Rouge pour une température supérieure à 30°C

# Fonction pour définir la couleur en fonction de l'humidité
def get_humidity_color(humid):
    if humid < 40:
        return (255, 0, 0)  # Rouge pour une humidité inférieure à 40%
    elif humid < 70:
        return (0, 255, 0)  # Vert pour une humidité entre 40% et 70%
    else:
        return (0, 0, 255)  # Bleu pour une humidité supérieure à 70%

# Fonction pour définir la couleur en fonction de la pression
def get_pressure_color(press):
    if press < 1000:
        return (255, 255, 0)  # Jaune pour une pression inférieure à 1000 hPa
    elif press < 1020:
        return (0, 255, 255)  # Cyan pour une pression entre 1000 et 1020 hPa
    else:
        return (255, 165, 0)  # Orange pour une pression supérieure à 1020 hPa

# Définir les couleurs pour chaque capteur
temp_color = get_temperature_color(temperature)
humidity_color = get_humidity_color(humidity)
pressure_color = get_pressure_color(pressure)

# Afficher les valeurs sur le terminal
print(f"Température : {temperature:.2f} °C (Couleur: {temp_color})")
print(f"Humidité : {humidity:.2f} % (Couleur: {humidity_color})")
print(f"Pression : {pressure:.2f} hPa (Couleur: {pressure_color})")

# Afficher les valeurs sur le Sense HAT LED matrix
# Créer un message avec des couleurs qui correspond aux capteurs
message = f"T:{temperature:.2f}C H:{humidity:.2f}% P:{pressure:.2f}hPa"
sense.show_message(message, text_colour=temp_color, back_colour=humidity_color)

# Afficher un écran LED coloré pour la pression
sense.clear(pressure_color)
# Importation des bibliothèques nécessaires
from sense_hat import SenseHat

# Initialisation de l'objet SenseHat
sense = SenseHat()

# Récupérer les valeurs des capteurs
temperature = sense.get_temperature()  # Température en Celsius
humidity = sense.get_humidity()       # Humidité relative en %
pressure = sense.get_pressure()       # Pression atmosphérique en hPa

# Affichage des valeurs
print(f"Température : {temperature:.2f} °C")
print(f"Humidité : {humidity:.2f} %")
print(f"Pression : {pressure:.2f} hPa")
