import pywhatkit
import flask
import pyautogui
import PySimpleGUI as sg
import socket

# Ventana con texto, boton start stop y enlace a la ip con puerto 8000
layout = [
          [sg.Text('Remote Control', size=(20, 1), font=("Helvetica", 25))],
          [sg.Text('IP: 0.0.0.0:8000', key='ip', size=(20, 1), font=("Helvetica", 15))],
          [sg.Text('', key='running', size=(20, 1), font=("Helvetica", 15))],
          [sg.Button('Start', size=(10, 1), font=("Helvetica", 15)), sg.Button('Stop', size=(10, 1), font=("Helvetica", 15))]
          ]

# Abrir la ventana
window = sg.Window('Remote Control', layout)

while True:
    event, values = window.read()
    if event in (None, "Stop"):
        pywhatkit.stop_server()
        window.close()
        break
    if event == 'Start':
        window.Element('Start').Update(disabled=True)
        ip = socket.gethostbyname(socket.gethostname())
        # Change window text
        window.Element('ip').Update('IP: ' + ip + ':8000')
        window.Element('running').Update('Server Running put this ip in your mobile browser')
        pywhatkit.start_server()
