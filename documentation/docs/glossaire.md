# Glossaire

## Rapsberry Pi Pico W
Microcôntroleur crée par la fondation Raspberry Pi. Programmable en C et en MicroPython. La variente W possède une puce WiFi et Bluethooth.

## Pico Explorer
Le Pico Explorer par Pimoroni est une base pour le Raspberry Pi Pico (W) qui intègre une breadboard avec des connecteur vers les GPIO, deux breakout pour des cartes compatbles et un écran avec 4 boutons dur les côtés.

## MQTT
MQTT est un rotocol de communication qui repose sur un sytème d'aboonement/sousctiption. Un client envoie sur un topic un message au serveur, aussi appelé broker, qui se charge ensuite de l'envoyer aux client qui eux se sont abbonés au même topic.

## broker
Un broker est un logicier qui se charge de recevoir des messages et de les propager à des clients qui le demande.

## InfluxDB
InfluxDB est un système de base de données dite TimeSeries, qui au lieu d'une base de données relationel classique (MariaDB par exemple), ne garde que les données récentes tandis que les données anciennes sont comprésées dans une moyenne.

## Telegraf
Telegraf est un module pour InfluxDB qui permet de récupérer des données MQTT et les ajouter automatiquement dans une base de données.