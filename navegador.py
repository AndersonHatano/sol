import sol
import navegadorClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

frase = sol.ouvir_microfone()



if(frase == "Google"):

    #Abri o navegador no site inicial de busca do Google
    navegadorClass.chrome.get(navegadorClass.google)

    #Aguarda até encontrar o elemento de busca
    elemento =  WebDriverWait(navegadorClass.chrome, 5).until(navegadorClass.aguardar_elemento_busca_google)

    frase = sol.ouvir_microfone()

    elemento.send_keys(frase)

    elemento.send_keys(Keys.ENTER)
    


elif(frase == "e-mail"):
    navegadorClass.chrome.get(navegadorClass.email)

elif(frase == "WhatsApp"):
    navegadorClass.chrome.get(navegadorClass.whatsapp)
