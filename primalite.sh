#!/bin/bash

# Vérifier si un argument est passé
if [ $# -ne 1 ]; then
    echo "Usage: $0 <nombre>"
    exit 1
fi

# Récupérer le nombre en argument
nombre=$1

# Vérifier si le nombre est inférieur à 2
if [ "$nombre" -lt 2 ]; then
    echo "$nombre n'est pas un nombre premier."
    exit 0
fi

# Boucle pour tester la divisibilité
for ((i=2; i*i<=nombre; i++)); do
    if [ $((nombre % i)) -eq 0 ]; then
        echo "$nombre n'est pas un nombre premier. Il est divisible par $i."
        exit 0
    fi
done

# Si aucune division n'a été trouvée
echo "$nombre est un nombre premier."

