from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chrome = webdriver.Chrome('C:\Fontes\chromedriver\chromedriver.exe')

email = 'https://www.gmail.com.br/'

google = 'https://www.google.com.br/'

whatsapp = 'https://web.whatsapp.com/'


def aguardar_elemento_busca_google(chrome):
    return chrome.find_element_by_name("q")
