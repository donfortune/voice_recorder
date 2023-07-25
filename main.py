import sounddevice as sd
import numpy as np

audio_data = np.array([19016586])
scaled_audio_data = np.int16(audio_data / np.max(np.abs(audio_data)) * 32767)
scaled_audio_data = scaled_audio_data.reshape(-1, 1)
print(scaled_audio_data)

fs = 44100
sd.play(scaled_audio_data, fs)