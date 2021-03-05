import time
import PySimpleGUI as sg
from ina260.controller import Controller


c=Controller(address=0x45)
volt = "%02.3f V" % (c.voltage())
now=time.localtime()

tt = "%04d-%02d-%02d  %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

layout = [[sg.Text(tt)],[sg.Text(volt)],[sg.Button("OK")]]


window = sg.Window("Check",layout)

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSE:
        break

window.close()
