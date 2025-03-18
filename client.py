import socket

# Configuration
hote = "127.0.0.1"  # Adresse du serveur (mettre IP du serveur si distant)
port = 12345

# Création du socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((hote, port))

# Saisie et envoi du message
message = input("Entrez le message à envoyer : ")
client.send(message.encode())

# Fermeture de la connexion
client.close()
