#!/usr/bin/env bash
#install a virtual environment
sudo pip3 install virtualenv
#add a virtual environment
virtualenv .venv
#run a virtual environment
source .venv/bin/activate

#install requirements.txt
pip install -r requirements.txt
