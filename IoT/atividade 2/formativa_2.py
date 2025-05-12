#ALUNO: Marcos Daniel Santana
#GRUPO: 270

import urequests
from wifi_lib import conecta
import urequests
import dht
import machine
import time

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)     # define o pino do rele como sinal de saida
WRITE_API_KEY = '76TCQUA5GTU3BWDH'  # chave de escrita (Write API Key)
cont = 16

#Conectando ao WIFI
print("Conectando...")
station = conecta("33robotics", "ponteaga")
if not station.isconnected():
    print("Não conectado!...")
else:
    print("Conectado!...")
    print("Acessando o site...")
    response = urequests.get("https://thingspeak.mathworks.com/channels/2925654")       #página para vizualização dos field de temperatura e umidade atraves do thing speak
    print("Página acessada:")
    print(response.text)

    while True:
        #lendo os sensores
        d.measure()
        print("Temperatura: {} | Umidade: {}".format(d.temperature(), d.humidity()))
        temp = d.temperature()          # armazena a temperatura
        hum = d.humidity()              # armazena a umidade	
        
        #Acionamento do rele:
        if(temp > 31 or hum > 70):  # liga o rele
            r.value(1)
        else:       # desligao rele
            r.value(0)
        
        if cont > 15:	# envia os dados para o thing speak a cada 15 segundos
            cont = 0
            # Envia temperatura e umidade no mesmo request
            url = 'https://api.thingspeak.com/update?api_key={}&field1={}&field2={}'.format(WRITE_API_KEY, temp, hum)
            response = urequests.get(url)

            if response.status_code == 200 and response.text != '0':
                print(f'Dado enviado com sucesso! Entrada nº {response.text}')
            else:
                print('Falha ao enviar os dados:', response.status_code, response.text)

            response.close()  # sempre bom liberar a memória
            
        time.sleep(1)       # espera um segundo
        cont += 1



