# Afficher la valeur d'une balance

Le but est d'afficher la valeur une balance faite avec un HX711 sur l'écran d'un Pico Explorer

## 2022.12.22
Je reçois le module sans les headers soudé, je le fait pendant la pause de midi

## 2023.01.06
Je comence le projet et je me rends compte que j'ai soudé la moitier des headers dans un sens différents, je tente de les désouder mais en vain.

Je finis par souder les fils de la balance sur les headers.

## 2023.01.07
Je regarde plus profondément comment utiliser le module.

Tous les tutoriels que je trouve disent d'installer une librairie, et je leurs donnent raison car il semble aoir beaucoup de code pour pouvoir l'utiliser.

## 2023.01.08
Je retente de désouder les headers mais je fini par les casser.

Mon frère trouve dans ses affaires une barre de headers et je les soudes, du même côté que les autres.

Une fois la librairie de la balance et de l'écrant ont été installées, le code tiens juste sur moins de 15 lignes.

## 2023.01.12
En montrant ce que j'ai fait, M.Bonvin me fait remarqué qu'il y a un mavais contact entre les fils de la balance et la breadboard, mais c'était juste le module que j'avais mis dnas le mauvais sens. En lui remontrant, il me demande de passer la valeur en non-signée car la balance retourne une force, et pas le sens de la balance.

Je cherche les spécification du ADC et je vois qu'il revoie une valeur 24 bit

M.Bonvin voit avec moi comment la librairie fonctionne, comment les différentes méthodes appelée fonctionnent. Quand on a essayer de faires queles modification au script, ça bloquait.

Après avoir enlevé le ficheir boot.py, le script fonctionne et changer le channer pour CHANNEL_A_64 et demander la valeur brute à la fonnction read() semble enlever les nombres négatifs.

# 2023.01.18
J'ai ajouter la définition de la tare au lancement et la conversion en grames dans l'affichage.

# 2023.01.19
J'ai corrigé le code pour calculer la valeur pour que l'arrondi se faire au bon endroit et ajouter un boutton pour rafaire la tare.

Je crée un petit site pour pouvoir tester l'envoie d'information avec des requêtes HTML.