from luma.core.interface.serial import spi
from luma.oled.device import SSD1331
from luma.core.render import canvas
import time

# Configuration de la communication SPI avec l'écran
#serial = spi(port=2, device=7, gpio_DC=12, gpio_RST=8, gpio_CS=1)  # Adapté selon votre configuration SPI
device = SSD1331(serial)

# Fonction pour dessiner des formes et du texte
def draw_shapes_and_text():
    with canvas(device) as draw:
        # Dessin d'un rectangle
        draw.rectangle((10, 10, 50, 30), outline="white", fill="black")
        
        # Dessin d'un cercle
        draw.ellipse((60, 10, 100, 50), outline="white", fill="black")
        
        # Dessin d'une ligne
        draw.line((10, 40, 100, 40), fill="white", width=2)
        
        # Affichage de texte
        draw.text((10, 50), "Hello, SPI!", fill="white")
        draw.text((10, 60), "luma.oled + SPI", fill="white")

# Boucle principale
while True:
    draw_shapes_and_text()
    time.sleep(2)  # Rafraîchissement toutes les 2 secondes

