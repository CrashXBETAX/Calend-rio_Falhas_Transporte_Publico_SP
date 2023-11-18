@echo off
python -m venv .venv
powershell -Command "if ($PSVersionTable) { Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; .venv\Scripts\Activate.ps1 } else { .venv\Scripts\activate }"
pip install Pillow selenium bs4
python Processamento_Python.py
echo O resultado foi salvo na pasta 'Resultado'. Por favor, abra um arquivo HTML correspondente ao ano e à linha que você selecionou anteriormente.
pause