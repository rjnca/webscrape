#!/bin/sh

export PATH=/home/ron/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

cd ~/Scripts/ziiscrape
pipenv run python webscrape.py
