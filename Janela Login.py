from ast import Break
from cgi import test
import time
from time import *
from webbrowser import WindowsDefault #Importando todas as funções da biblioteca time
import selenium #Importando a biblioteca selenium
from selenium import webdriver #Importando o modulo Webdriver da biblioteca selenium
from selenium.webdriver.common.keys import Keys #Importando as Keys do modulo Webdriver
import PySimpleGUI as sg

#Criando o lyout
def Criar_janela_inicial():
    sg.theme('Reddit')
    linha = [
        [sg.Text('Usuario:'),sg.Input('',key='Usuario',size=(15,1)),sg.Text('Password:'),sg.Input('',key='Password',size=(15,1), password_char='*')]
    ]
    layout = [
        [sg.Frame('Dados de Login',layout=linha,key='continer')],
        [sg.Button('Proximo')]
    ]
    return sg.Window('Todo List',layout=layout,finalize=True)

def Tela_de_links():
    linha = [
        [sg.Text('Link 1'),sg.Input('',key='Link1',size=(45,1))],
        [sg.Text('Link 2'),sg.Input('',key='Link2',size=(45,1))],
        [sg.Text('Link 3'),sg.Input('',key='Link3',size=(45,1))],
        [sg.Text('Link 4'),sg.Input('',key='Link4',size=(45,1))],
        [sg.Text('Link 5'),sg.Input('',key='Link5',size=(45,1))],
        [sg.Text('Link 6'),sg.Input('',key='Link6',size=(45,1))],
    ]
    layout = [
        [sg.Frame('Links dos Posts',layout=linha,key='contiener')],
        [sg.Button('Proximo'), sg.Button('Voltar')]
    ]
    return sg.Window('Links Instagram',layout=layout,finalize=True)

def Tela_de_comentarios():
    linha = [
        [sg.Text('1º'),sg.Input('',key='Comentario1',size=(21,1)),sg.Text('5º'),sg.Input('',key='Comentario5',size=(21,1))],
        [sg.Text('2º'),sg.Input('',key='Comentario2',size=(21,1)),sg.Text('6º'),sg.Input('',key='Comentario6',size=(21,1))],
        [sg.Text('3º'),sg.Input('',key='Comentario3',size=(21,1)),sg.Text('7º'),sg.Input('',key='Comentario7',size=(21,1))],
        [sg.Text('4º'),sg.Input('',key='Comentario4',size=(21,1)),sg.Text('8º'),sg.Input('',key='Comentario8',size=(21,1))],
    ]
    layout = [
        [sg.Frame('Comentarios a ser publicados',layout=linha,key='contiener')],
        [sg.Button('Iniciar'), sg.Button('Voltar')]
    ]
    return sg.Window('Comentarios', layout=layout,finalize=True)

#Cria a janela
tela_login, tela_links, tela_comentarios = Criar_janela_inicial(), None, None
#tela_links = Tela_de_links()
#janela3 = Tela_de_comentarios()
#Criar as regras da janela
while True:
    window, event, values = sg.read_all_windows()
    if window == tela_login and event == sg.WIN_CLOSED:
        break
    elif window == tela_login and event == 'Proximo':
        tela_login.hide()
        tela_links = Tela_de_links()
    elif window == tela_links and event == sg.WIN_CLOSED:
        break
    elif window == tela_links and event == 'Voltar':
        tela_links.hide()
        tela_login.un_hide()
    elif window == tela_links and event == 'Proximo':
        tela_links.hide()
        tela_comentarios = Tela_de_comentarios()
    elif window == tela_comentarios and event == sg.WIN_CLOSED:
        break
    elif window == tela_comentarios and event == 'Voltar':
        tela_comentarios.hide()
        tela_links.un_hide()
    