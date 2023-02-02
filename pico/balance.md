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

## 2023.01.18
J'ai ajouter la définition de la tare au lancement et la conversion en grames dans l'affichage.

## 2023.01.19
J'ai corrigé le code pour calculer la valeur pour que l'arrondi se faire au bon endroit et ajouter un boutton pour rafaire la tare.

Je crée un petit site pour pouvoir tester l'envoie d'information avec des requêtes HTML.

## 2023.01.26
J'essaie de me transmettre des informations entre le pico est une page php en local, mais les deux ne sont pas sur le même réseau, et les clés WiFi dans la salle ne sont pas reconnues par Ubuntu (merci les drivers propriétaires)

J'ai suivi des instructions sur comment installer des drivers pour la clé, et je peux enfi l'utiliser.

J'ai demander de l'aide à M. Bonvin sur comment envoyer les données du pico au serveur, et il m'a remis sur la bonne piste et au lieu d'utiliser une page PHP, je fait directent du MQTT. Il m'a guidé sur l'installation de Mosquitto et m'a donné un lien vers [un tutoriel sur la configuration et comment comminquer avec un Pico.](https://peppe8o.com/mqtt-and-raspberry-pi-pico-w-start-with-mosquitto-micropython/)

Je regarde les script qui y sont fournis pour les comprendre.

## 2023.02.01
J'installe Mosquitto MQTT sur un Raspberry Pi mais qunad il s'agit de connect le Pico à celui-ci, je ne sait pas pourquoi, ça bloque. J'ai essaayer l'IP de l?Ethernet, du WiFi et son nom de domaine local mais ça bloque à l'étape de connexion au broker.

J'ai débranché rebranché le Pico est tout est réglé.

J'ai ajouté un module pour gérer les intérations avec le broker. Le problème est que le code est syncrone, ce qui fait que l'écran se recharge en même temps que l'envoi. Il faut que je rende le code asyncrone.
Je crée un petit site connécté à une basse do données pour pouvoir tester l'envoie d'information avec des requêtes HTML.