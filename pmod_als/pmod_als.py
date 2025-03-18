import spidev
import time

# Configuration SPI
SPI_MODE = 0  # Mode SPI 0 (PMOD-ALS)
SPI_SPEED = 2000000  # 2 MHz

# Initialisation du SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, périphérique 0 (CE0)
spi.max_speed_hz = SPI_SPEED
spi.mode = SPI_MODE

def read_light():
    """Lit la valeur de luminosité du PMOD-ALS."""
    buff2 = spi.xfer2([0x00, 0x00])  # Envoi et réception de 2 octets
    lightvalue = (buff2[0] << 3) | (buff2[1] >> 4)  # Reconstruction des 12 bits utiles
    return lightvalue

try:
    while True:
        lumiere = read_light()
        print(f"Lumière : {lumiere}")
        time.sleep(1)  # Pause d'une seconde

except KeyboardInterrupt:
    print("Arrêt du programme.")
    spi.close()  # Fermer le SPI proprement
