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
        [sg.Text('Usuario:'),sg.Input('',key='Usuario',size=(15,1)),sg.Text('Password:'),sg.Input('',key='Password',size=(15,1))]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='continer')],
        [sg.Button('Proximo')]
    ]
    return sg.Window('Todo List',layout=layout,finalize=True)

def Tela_de_links():
    linha = [
        [sg.Text('Link 1'),sg.Input('',key='Usuario',size=(45,1))],
        [sg.Text('Link 2'),sg.Input('',key='Usuario',size=(45,1))],
        [sg.Text('Link 3'),sg.Input('',key='Usuario',size=(45,1))],
        [sg.Text('Link 4'),sg.Input('',key='Usuario',size=(45,1))],
        [sg.Text('Link 5'),sg.Input('',key='Usuario',size=(45,1))],
        [sg.Text('Link 6'),sg.Input('',key='Usuario',size=(45,1))],
    ]
    layout = [
        [sg.Frame('Links',layout=linha,key='contiener')],
        [sg.Button('Proximo')]
    ]
    return sg.Window('Links Instagram',layout=layout,finalize=True)

#Cria a janela
janela = Criar_janela_inicial()
janela2 = Tela_de_links()
#janela2 = Janela_test()
#Criar as regras da janela
while True:
    event, values = janela.read()
    event, values = janela2.read()
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