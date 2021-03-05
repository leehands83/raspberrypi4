import PySimpleGUI as sg

layout = [[sg.Text("Hello from PysimpleGUI")],[sg.Button("OK")]]


window = sg.Window("Check",layout)

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSE:
        break

window.close()
