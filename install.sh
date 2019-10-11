#!/bin/bash



##Instala as de pendencias aqui
sudo apt-get update
sudo apt-get install -y motion
sudo apt-get install -y sysvbanner
sudo apt-get install -y python3.7
python3.7 -m pip install pip
pip3 install twilio


# PRA EXECUTAR O SCRIPT EM PYTHON É O MESMO COMANDO

sudo chmod +x run.sh
