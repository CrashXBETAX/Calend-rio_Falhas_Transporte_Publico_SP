import os
class CriarImageTodosMeses:
    @staticmethod
    def RenderizandoImage(html, linha, ano):
        html_filename = f'Resultado/resultado_{ano}_{linha}.html'
        with open(html_filename, 'w', encoding='utf-8') as html_file:
            html_file.write(html)
    @staticmethod
    def CriandoImage(linha, ano):
        with open('template.html', 'r', encoding='utf-8') as arquivo:
            conteudo_html = arquivo.read()
        if linha < 4 or linha == 15:
            empresa = "Metro"
        elif linha == 4:
            empresa = "ViaQuatro"
        elif linha == 8 and ano < 2022:
            empresa = "CPTM"
        elif linha == 8:
            empresa = "ViaMobilidade"
        elif linha == 9 and ano < 2022:
            empresa = "CPTM"
        elif linha == 9:
            empresa = "ViaMobilidade"
        elif linha == 5 and ano < 2018:
            empresa = "Metro"
        elif linha == 5:
            empresa = "ViaMobilidade"
        elif 10 <= linha < 14 or linha == 7:
            empresa = "CPTM"
        if linha == 1:
            nome_linha = f"Linha {linha} - Azul"
            color = "#171796"
        elif linha == 2:
            nome_linha = f"Linha {linha} - Verde"
            color = "#007A5E"
        elif linha == 3:
            nome_linha = f"Linha {linha} - Vermelha"
            color = "#ED2E38"
        elif linha == 4:
            nome_linha = f"Linha {linha} - Amarela"
            color = "#FFD525"
        elif linha == 5:
            nome_linha = f"Linha {linha} - Lilas"
            color = "#BA1FB5"
        elif linha == 7:
            nome_linha = f"Linha {linha} - Rubi"
            color = "#AC184A"
        elif linha == 8:
            nome_linha = f"Linha {linha} - Diamante"
            color = "#AFA690"
        elif linha == 9:
            nome_linha = f"Linha {linha} - Esmeralda"
            color = "#34AEA4"
        elif linha == 10:
            nome_linha = f"Linha {linha} - Turquesa"
            color = "#17839C"
        elif linha == 11:
            nome_linha = f"Linha {linha} - Coral"
            color = "#EB601F"
        elif linha == 12:
            nome_linha = f"Linha {linha} - Safira"
            color = "#1C5B81"
        elif linha == 13:
            nome_linha = f"Linha {linha} - Jade"
            color = "#00A150"
        elif linha == 15:
            nome_linha = f"Linha {linha} - Prata"
            color = "#8F8F8C"
        conteudo_html = conteudo_html.replace("{empresa}", empresa)
        conteudo_html = conteudo_html.replace("{ano}", str(ano))
        conteudo_html = conteudo_html.replace("{num}", str(linha))
        conteudo_html = conteudo_html.replace("{color}", color)
        conteudo_html = conteudo_html.replace("{Nome_Linha}", nome_linha)
        CriarImageTodosMeses.RenderizandoImage(conteudo_html, linha, ano)