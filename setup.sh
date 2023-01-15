#! /bin/bash

if ! [ -d ".env" ];
then
    python3 -m venv .env
fi

. .env/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
