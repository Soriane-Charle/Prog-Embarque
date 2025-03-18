#!/bin/bash

# Vérifier si un fichier est fourni en argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <fichier>"
    exit 1
fi

# Vérifier si le fichier existe
if [ ! -f "$1" ]; then
    echo "Erreur : Le fichier $1 n'existe pas."
    exit 1
fi

# Supprimer les retours chariot Windows (^M)
sed -i 's/\r//g' "$1"

echo "Conversion terminée : $1 est maintenant au format UNIX."
