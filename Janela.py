import time
from time import * #Importando todas as funções da biblioteca time
import selenium #Importando a biblioteca selenium
from selenium import webdriver #Importando o modulo Webdriver da biblioteca selenium
from selenium.webdriver.common.keys import Keys #Importando as Keys do modulo Webdriver
import PySimpleGUI as sg
import Bot comentarios instagram

#Criando o lyout
def Criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''),sg.Input('')]]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='continer')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]]

    return sg.Window('Todo List',layout=layout,finalize=True)
#Cria a janela
janela = Criar_janela_inicial()
#Criar as regras da janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['continer'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = Criar_janela_inicial()