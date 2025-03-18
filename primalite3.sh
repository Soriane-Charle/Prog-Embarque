#!/bin/bash
# Optimisation pour la verification d'un nombre premier

if [ $# -ne 1 ]; then
    echo "Erreur : Vous devez passer un seul nombre en paramètre."
    exit 1
fi

if ! echo "$1" | grep -qE '^[0-9]+$'; then
    echo "Erreur : Le paramètre doit être un nombre entier positif."
    exit 1
fi

num=$1

if [ "$num" -lt 2 ]; then
    echo "$num n'est pas un nombre premier."
    exit 0
fi

is_prime=1
diviseurs=""

for (( i=2; i<=num/2; i++ )); do
    if [ $(( num % i )) -eq 0 ]; then
        is_prime=0
        diviseurs="$diviseurs $i"
    fi
done

if [ "$is_prime" -eq 1 ]; then
    echo "$num est un nombre premier."
else
    echo "$num n'est pas un nombre premier. Ses diviseurs sont :$diviseurs"
fi

