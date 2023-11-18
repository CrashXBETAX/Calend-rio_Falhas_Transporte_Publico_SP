from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup
class ExtrairHTML(object):
    def ExtraindoHTML(linha, ano):
        driver = webdriver.Chrome()
        url = "https://www.diretodostrens.com.br/?codigo=" + str(linha) + "&ano=" + str(ano)
        driver.get(url)
        last_height = driver.execute_script("return document.body.scrollHeight")
        page_height = 0
        scroll_pause_time = 0.75
        while True:
            driver.execute_script("window.scrollTo(0, " + str(page_height) + ");")
            time.sleep(scroll_pause_time)
            page_height += 500
            new_height = driver.execute_script("return document.body.scrollHeight")
            if page_height >= last_height:
                break
            last_height = new_height
            last_height = driver.execute_script("return document.body.scrollHeight")
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        if not os.path.exists("HTML_Salvos"):
            os.makedirs("HTML_Salvos")
        with open('HTML_Salvos/linha_' + str(linha) + '_ano_' + str(ano)+ '.html', 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        print('HTML salvo com sucesso!')