import time #Importando a biblioteca time
from time import * #Importando todas as funções da biblioteca time
import selenium #Importando a biblioteca selenium
from selenium import webdriver #Importando o modulo Webdriver da biblioteca selenium
from selenium.webdriver.common.keys import Keys #Importando as Keys do modulo Webdriver
from tkinter import *

print("Hello Word")

class InstagramBot:
    def __init__(self,Username,Password):
        self.Username = Username
        self.Password = Password
        self.driver = webdriver.Chrome(executable_path='D:\Programação\Codigos\Bot comentarios instagram\chromedriver.exe') #Local onde se encontra o .EXE do Webdriver

    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/') #Site para onde o Webdriver vai navegar
        sleep(5)
        Campo_usuario = driver.find_element_by_name('username') #Localizando o campo Username 
        Campo_usuario.click()
        Campo_usuario.clear()
        Campo_usuario.send_keys(self.Username) #Mandado enviar o conteudo do campo username, conteudo informado na penultima linha
        sleep(1)
        Campo_senha = driver.find_element_by_name('password') #Localizando o campo Password
        Campo_senha.click()
        Campo_senha.clear()
        Campo_senha.send_keys(self.Password) #Mandado enviar o conteudo do campo password, conteudo informado na penultima linha
        sleep(1)
        Campo_senha.send_keys(Keys.ENTER) #Enviando o comando de aperta o enter
        sleep(10)
        
        driver.get('https://www.instagram.com/p/CY2W-7MLngp/') #link do post que e para comentar 
        sleep(5)

        for numero in range(5):
            driver.find_element_by_class_name('Ypffh').click() #Localizando o campo comentario
            Campo_comentario = driver.find_element_by_class_name('Ypffh')
            Campo_comentario.click()
            Campo_comentario.clear()
            Campo_comentario.send_keys('@bruna_kemillysouza') #Enviando texto a ser comentado
            sleep(1)
            for numero in range(3):
                Campo_comentario.send_keys(Keys.ENTER) #Enviando o comando de aperta o enter
            sleep(10)

VEGO = InstagramBot('vegotest52','88195104aA')
VEGO.Login()