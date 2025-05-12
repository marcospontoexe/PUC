#ALUNO: Marcos Daniel Santana
#GRUPO: 270
import network
import time

def conecta(ssid, senha):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station

