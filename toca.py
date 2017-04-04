#!/usr/bin/env python3
import subprocess
import time

musica = subprocess.Popen(['mpg123', '-q', '/home/chip/Music/Maskavo-Anjo do Céu.mp3'])
time.sleep(5)
musica.terminate()
