from PIL import ImageFont
from luma.oled.device import ssd1331
from luma.core.render import canvas
from DesignSpark.Pmod.HAT import createPmod
import RPi.GPIO as gpio

gpio.setwarnings(False)


# Fonction pour diviser le texte en lignes

def wrap_text(text, font, max_width):
    lines = []
    words = text.split(' ')
    current_line = words[0]

    for word in words[1:]:
        # Vérifie si le mot ajouté dépasse la largeur de l'écran
        if font.getbbox(current_line + ' ' + word)[0] <= max_width:
            current_line += ' ' + word
        else:
            # Si ça dépasse, ajouter la ligne actuelle et commencer une
            # nouvelle ligne
            lines.append(current_line)
            current_line = word

    lines.append(current_line)  # Ajouter la dernière ligne
    return lines


if __name__ == '__main__':
    try:
        oled = createPmod('OLEDrgb', 'JA')
        device = oled.getDevice()

        # Charger une police pour le texte
        font = ImageFont.load_default()

        # Calculer la largeur maximale de l'écran
        max_width = device.width
        max_height = device.height

        # Le texte à afficher
        text = "Hello Soso and Kim"

        # Diviser le texte en lignes
        lines = wrap_text(text, font, max_width)

        # Afficher chaque ligne sur l'écran OLED
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")

            # Position de départ pour le texte
            y_offset = 2  # Démarrer à 2 pixels en Y
            for line in lines:
                if y_offset + font.getbbox(line)[1] > max_height:
                    break
            draw.text((2, y_offset), line, fill="white")
            # Augmenter l'offset Y pour la ligne suivante
            y_offset += font.getbbox(line)[1]

	    # Afficher des formes sur l'écran
            draw.rectangle([10, 10, 80, 40], outline="white", fill="blue")  # Rectangle
            draw.ellipse([20, 30, 30, 40], outline="white", fill="green")  # Cercle

        # Boucle infinie pour maintenir l'affichage
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        oled.cleanup()
