from cgi import test
from selenium import *
from selenium import webdriver

print("Hello Word")

class InstagramBot:
    def __init__(self,Username,Password):
        self.Username = Username
        self.Password = Password
        self.driver = webdriver.Chrome(executable_path='D:\Programação\Codigos\Bot comentarios instagram\chromedriver.exe')

    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')

VEGO = InstagramBot('vegotest52','88195104aA')
VEGO.Login()