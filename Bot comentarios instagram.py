from cgi import test
import time
from time import *
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Hello Word")

class InstagramBot:
    def __init__(self,Username,Password):
        self.Username = Username
        self.Password = Password
        self.driver = webdriver.Chrome(executable_path='D:\Programação\Codigos\Bot comentarios instagram\chromedriver.exe')

    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        sleep(5)
        Campo_usuario = driver.find_element_by_name('username')
        Campo_usuario.click()
        Campo_usuario.clear()
        Campo_usuario.send_keys(self.Username)
        sleep(1)
        Campo_senha = driver.find_element_by_name('password')
        Campo_senha.click()
        Campo_senha.clear()
        Campo_senha.send_keys(self.Password)
        sleep(1)
        Campo_senha.send_keys(Keys.ENTER)
        sleep(10)

VEGO = InstagramBot('vegotest52','88195104aA')
VEGO.Login()