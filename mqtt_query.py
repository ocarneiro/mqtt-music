import paho.mqtt.client as mq
import subprocess
from glob import glob
import random
import os

player = None
musicas = glob("/home/chip/Music/*.mp3")
print("Há %d músicas na biblioteca" % len(musicas))

def on_connect(client, userdata, flags, rc):
    print("Conectado! Código:" + str(rc))
    client.subscribe("musica")

def on_message(client, userdata, msg):
    global player
    if player:
        player.terminate() 
    pedido = msg.payload.decode('utf-8')
    selecionadas = [m for m in musicas if pedido.lower() in m.lower()]
    print("Encontrei %d músicas"%len(selecionadas))
    if len(selecionadas) > 0:
        musica = random.choice(selecionadas)
        print("Selecionei: %s" % os.path.basename(musica))
        player = subprocess.Popen(['mpg123', '-q',
                                  musica])
    print(msg.topic + ":" + str(msg.payload))

if __name__ == '__main__':
    cli = mq.Client()
    cli.on_connect = on_connect
    cli.on_message = on_message
    cli.connect("192.168.25.150", 1883, 60)
    cli.loop_forever()
