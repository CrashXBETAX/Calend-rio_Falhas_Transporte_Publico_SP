import re
class TratamentoDados(object):
    def TratandoDados(linha, ano):
        with open('HTML_Salvos/linha_' + str(linha) + '_ano_' + str(ano)+ '.html', 'r', encoding='utf-8') as arquivo:
            conteudo_html = arquivo.read()
        regex = r"<tr class=\"(.*)\"\sid[^>]*>\s*<td>\s*<a[^>]*>\s*([\d\/: ]+)\s\d{2}:"
        matches = re.finditer(regex, conteudo_html, re.MULTILINE)
        resultados = []
        for match in matches:
            grupo1 = match.group(1)
            grupo2 = match.group(2)
            if grupo1 != "table-success" and grupo1 != "table-info":
                resultados.append((grupo1, grupo2))
        return resultados