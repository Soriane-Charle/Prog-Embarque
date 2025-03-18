#!/bin/sh
# Script qui vérifie la parité d'un nombre

# Vérification du nombre de paramètres
if [ $# -ne 1 ]; then
    echo "Erreur : Vous devez passer un seul paramètre (un nombre entier)."
    exit 1
fi

# Vérification que le paramètre est un entier
if ! echo "$1" | grep -qE '^-?[0-9]+$'; then
    echo "Erreur : Le paramètre doit être un nombre entier."
    exit 1
fi

# Vérification de la parité
if [ $(( $1 % 2 )) -eq 0 ]; then
    echo "Le nombre $1 est pair."
else
    echo "Le nombre $1 est impair."
fi
