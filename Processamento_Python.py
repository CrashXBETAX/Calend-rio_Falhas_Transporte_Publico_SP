from CriarImageTodosMeses import CriarImageTodosMeses
from CriarImagem import CriarImagem
from ExtrairHTML import ExtrairHTML
from TratamentoDados import TratamentoDados
linhas_validas = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15]
anos_validos = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
linhas_escolhidas = input("Digite as linhas desejadas (separadas por vírgula): ")
anos_escolhidos = input("Digite os anos desejados (separados por vírgula): ")
linhas_usuario = [int(linha) for linha in linhas_escolhidas.split(',')]
anos_usuario = [int(ano) for ano in anos_escolhidos.split(',')]
linhas_invalidas = [linha for linha in linhas_usuario if linha not in linhas_validas]
anos_invalidos = [ano for ano in anos_usuario if ano not in anos_validos]
if linhas_invalidas:
    print("As seguintes linhas são inválidas:", linhas_invalidas)
if anos_invalidos:
    print("Os seguintes anos são inválidos:", anos_invalidos)
if not linhas_invalidas and not anos_invalidos:
    for linha in linhas_usuario:
        for ano in anos_usuario:
            ExtrairHTML.ExtraindoHTML(linha, ano)
            CriarImagem.CriandoImage(TratamentoDados.TratandoDados(linha, ano), linha, ano)
            CriarImageTodosMeses.CriandoImage(linha, ano)
else:
    print("Por favor, insira somente linhas e anos válidos.")