import socket

# Configuration
hote = "0.0.0.0"  # Accepte les connexions sur toutes les interfaces
port = 12345  # Port d'écoute

# Création du socket
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((hote, port))
serveur.listen(1)

print(f"Serveur en attente de connexion sur {hote}:{port}...")

# Acceptation de la connexion
client_socket, client_adresse = serveur.accept()
print(f"Connexion établie avec {client_adresse}")

# Réception des données
data = client_socket.recv(1024).decode()
print(f"Message reçu : {data}")

# Fermeture des connexions
client_socket.close()
serveur.close()

