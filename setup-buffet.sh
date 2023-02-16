#!/bin/bash
#Script      : setup-buffet
#Description : Sets up a Raspberry Pi OS installation with mosquitto and InfluxDB
#Author      : DOMINGUES PEDROSA Samuel
#Date        : 2023.02.08, V1.0

sudo apt update
sudo apt upgrade -y
sudo apt install mosquitto mosquitto-clients apt-transport-https vim -y

# Setup Mosquitto
sudo mosquitto_passwd -b -c /etc/mosquitto/passwd buffet tastybuffet
printf "allow_anonymous false\nlistener 1883\npassword_file /etc/mosquitto/passwd" | sudo tee -a /etc/mosquitto/mosquitto.conf
sudo systemctl restart mosquitto.service

# Add InfluxDB repo
wget -q https://repos.influxdata.com/influxdata-archive_compat.key
echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list

# Install and start InfluxDB
sudo apt-get update && sudo apt-get install influxdb
sudo systemctl unmask influxdb.service
sudo systemctl start influxdb

# Add Telegraf repo
wget -qO- https://repos.influxdata.com/influxdata-archive_compat.key | sudo apt-key add -
source /etc/os-release
echo "deb https://repos.influxdata.com/debian buster stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

# Install Telegraf
sudo apt-get update && sudo apt-get install telegraf
