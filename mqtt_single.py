import paho.mqtt.client as mq
import subprocess

player = None

def on_connect(client, userdata, flags, rc):
    print("Conectado! Código:" + str(rc))
    client.subscribe("musica")

def on_message(client, userdata, msg):
    global player
    if not player:
        player = subprocess.Popen(['mpg123', '-q', '/home/chip/Music/Maskavo-Anjo do Céu.mp3'])
    else:
        player.terminate()
    print(msg.topic + ":" + str(msg.payload))

if __name__ == '__main__':
    cli = mq.Client()
    cli.on_connect = on_connect
    cli.on_message = on_message
    cli.connect("192.168.25.150", 1883, 60)
    cli.loop_forever()
