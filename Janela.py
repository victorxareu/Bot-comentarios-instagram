from cgi import test
import time
from time import * #Importando todas as funções da biblioteca time
import selenium #Importando a biblioteca selenium
from selenium import webdriver #Importando o modulo Webdriver da biblioteca selenium
from selenium.webdriver.common.keys import Keys #Importando as Keys do modulo Webdriver
import PySimpleGUI as sg

#Criando o lyout
def Criar_janela_inicial():
    sg.theme('Reddit')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='continer')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar'), sg.Button('Nova janela')]
    ]
    return sg.Window('Todo List',layout=layout,finalize=True)

def Janela_test():
    sg.theme('Reddit')
    linha = [
        [sg.Checkbox('',key='chec'), sg.Input(key='te')]
    ]
    layout = [
        [sg.Frame('Janela 2', layout=linha, key='test')],
        [sg.Button('Test')]
    ]
    return sg.Window('Test', layout=layout, finalize=True)

#Cria a janela
janela = Criar_janela_inicial()
#janela2 = Janela_test()
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
    elif event == 'Nova janela':
        janela2 = Janela_test()
        janela.close()
        
    while True:
        event, values = janela2.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Test':
            if values['chec'] == 1:
                janela2.close()
            else:
                janela2.close()
                janela = Criar_janela_inicial()