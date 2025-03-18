#!/bin/sh
# Script qui affiche les paramètres passés en ligne de commande

echo "Nombre de paramètres : $#"
echo "Liste des paramètres : $@"

# Affichage individuel des paramètres
i=1
for param in "$@"; do
    echo "Paramètre $i : $param"
    i=$((i+1))
done
