#!/bin/sh
# Script qui crée un dossier, se déplace dedans, crée un fichier et y stocke la date courante

# Création du répertoire folder
mkdir -p folder

# Se déplacer dans folder
cd folder || exit

# Création du fichier file
touch file

# Stocker la date courante dans file
date > file

# Afficher un message de confirmation
echo "Le dossier 'folder' a été créé, la date actuelle a été enregistrée dans 'file'."

