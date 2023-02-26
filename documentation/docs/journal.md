# Journal de bord des PoCs

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

## 2023.02.02
Hier, quand je rangeais le matériel, le fil du A+ s'est détaché du header, et le connecter directement à une breadboard ne marche pas. Et le fil rouge aussi ce matin...

J'ai dit à M. Bonvin que je dois resouder les fils, et il m'a guidé sur comment bien souder, utiliser des gaines, étaner les fils en chauffant le fils puis en le passant dans l'étain, etc... Il m'as aussi dit de soit trouver des câbles de bonnes couleurs, soit de faire une commande au près de M. Garcia.

Après avoir cherché la classe, je doit passer une commande.

J'ai passé commande auprès de M. Garcia et je regarde comme fonctionne `asyncio`

## 2023.02.08
Je tente d'installer InfluxDB sur un Raspberry Pi mais je n'ai pas `influx` pour pouvoir intéragir avec.

J'ai du réinstaller le serveur pour pouvoir correctement installer InfluxDB.

J'ai réinstallé InfluxDB avec un [tutoriel plus récent](https://docs.influxdata.com/influxdb/v2.6/install/?t=Linux) mais ça me dit que les ports sont déjà utilisés.


## 2023.02.09
Je suis [un autre tuto](https://randomnerdtutorials.com/install-influxdb-2-raspberry-pi/).

J'ai resussi à créer un utilisateur et un bucket, l'équivalent d'une table.

Je regarde dans la doc comment l'[utiliser avec Python](https://docs.influxdata.com/influxdb/v2.6/api-guide/client-libraries/python/#) mais le nom du module est incorrect.

La doc était incorreecte, j'ai trouvé une [documentation correct](https://www.influxdata.com/blog/getting-started-python-influxdb/), j'arrive à me connecter, mais pas à aller répupérer la liste des bases de données.

M.Bonvin m'a ramené le livre MQTT et j'y vois que la version du livre n'est pas la plus récente (1.8 contre 2.6).

Il me donne aussi deux Pico, un avec un capteur de température & d'humidité, et l'autre avec un capteur de mouvement, avec le programme connecté à un broker.

# 2023.02.14
J'ai suivi [la documentation de la version du livre](https://docs.influxdata.com/influxdb/v1.8/introduction/install/).

# 2023.02.15
Je peux pas me connecter au broker, que se soit mon code ou celuis des Picos que M.Bonvin m'a donné. Le broker est installé, le nom du serveur et les identifiants sont corrects, et ça ne se connecte pas.

Le syntaxe d'insertion du livre semble fausse, quand je recopie les lignes d'exemple, on me donne une erreur 'missing fields'.

Problème de lecture, à la plce de l'espace qui sépare la table et les tags des champs, il y a un retour à la ligne...

Un fait intéréssant avec les tables est qu'elles sont crées à la volée.

## 2023.02.16
Dans mon script de configuration de serveur, j'ai oublié d'ajouter `listener 1883` au fichier de configuration.

Je dois réinstaller InfluxDb, et cette fois-ci, la version la plus récente car je ne paux pas installer le version de Telegraf que je veux.

## 2023.02.24
J'ai suivi le tutoriel de la documentsion **à la lettre**, ce que ne faisait pas avant car je séléctionnait les instructions Ubuntu/Debian alors que j'aurais du télécharger les binaires et ensuite les installer avec dpkg, mais maintenant j'ai InfluxDB et le client à la version la plus récente, 2.6.

## 2023.02.26
J'ai installé Telegraf 1.16.3 et j'ai aucun problèmes. Le seul point blocant pourrait être InfluxDB 2.6 qui aurais la v1 de l'aout des données désactivée voir enlevée.

Il faut que j'installe une version pré 2.0 pour utiliser l'input v1.

J'ai réussi. J'ai dû utiliser les version d'InfluxDB et de Telegraf du livre mais j'ai réussi à alimenter une base de données depuis un broker MQTT.