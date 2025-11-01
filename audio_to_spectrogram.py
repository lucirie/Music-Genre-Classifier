import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

# Open 'songs' folder and itterate over each .wav file
import os

directory = os.fsencode('songs')

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith('.wav'):
        # Convert into spectrogram
        sample_rate, samples = wavfile.read(file)
        frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
        continue
    else:
        print("non-wav audiofiles not supported")