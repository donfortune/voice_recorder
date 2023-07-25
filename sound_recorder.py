import sounddevice
from scipy import write

fs = 44100

time = int(input('Enter your recording time in seconds:'))
print('Recording has started...')
record = sounddevice.rec(int(time *fs), samplerate=fs, channels=2)
sounddevice.wait()
write("audio.wave",fs,record)
print("Recording dodne!! check your download folder")
