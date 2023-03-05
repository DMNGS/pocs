#!/bin/bash
# Script      : setup-buffet
# Description : Sets up a Raspberry Pi OS installation with mosquitto, InfluxDB and Telegraf
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2023.02.08, V1.0

sudo apt update
sudo apt upgrade -y

# Install mosquitto MQTT (and vim)
sudo apt install mosquitto mosquitto-clients vim -y

# Setup Mosquitto
sudo mosquitto_passwd -c -b /etc/mosquitto/passwd buffet

printf "allow_anonymous false\npassword_file /etc/mosquitto/passwd\nlistener 1883" | sudo tee -a /etc/mosquitto/mosquitto.conf

sudo systemctl restart mosquitto.service

# Download and setup InfluxDB
wget -q https://repos.influxdata.com/influxdata-archive_compat.key
echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list

sudo apt-get update && sudo apt-get install influxdb
sudo systemctl unmask influxdb.service
sudo systemctl start influxdb

# Install Telegraf
wget https://dl.influxdata.com/telegraf/releases/telegraf_1.16.3-1_arm64.deb
sudo dpkg -i telegraf_1.16.3-1_arm64.deb

printf "\n###################\nSetup InfluxDB and Telegraf to be done manually\n###################\n"