#!/bin/bash
# Verification si un nombre est premier et afficher ses diviseurs

# Vérification du nombre de paramètres
if [ $# -ne 1 ]; then
    echo "Erreur : Vous devez passer un seul nombre en paramètre."
    exit 1
fi

# Vérification que l'entrée est un entier positif
if ! echo "$1" | grep -qE '^[0-9]+$'; then
    echo "Erreur : Le paramètre doit être un nombre entier positif."
    exit 1
fi

num=$1

# 0 et 1 ne sont pas premiers
if [ "$num" -lt 2 ]; then
    echo "$num n'est pas un nombre premier."
    exit 0
fi

# Vérification de la primalité et affichage des diviseurs
is_prime=1
diviseurs=""

for (( i=2; i*i<=num; i++ )); do
    if [ $(( num % i )) -eq 0 ]; then
        is_prime=0
        diviseurs="$diviseurs $i"
    fi
done

# Affichage du résultat
if [ "$is_prime" -eq 1 ]; then
    echo "$num est un nombre premier."
else
    echo "$num n'est pas un nombre premier. Ses diviseurs (hors 1 et lui-même) sont :$diviseurs"
fi

