#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install Pillow selenium bs4
python3 Processamento_Python.py
echo "O resultado foi salvo na pasta 'Resultado'. Por favor, abra um arquivo HTML correspondente ao ano e à linha que você selecionou anteriormente."
read -p "Pressione [Enter] para continuar..."