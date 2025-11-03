import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile

# Open 'songs' folder and itterate over each .wav file
import os
from pydub import AudioSegment

directory = os.fsencode('songs')

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith('.wav'):
        # Trim first 30 seconds of audio
        input_path = f'songs/{filename}'
        trimmed_path = f'trimmed_songs/{filename}'
        audio = AudioSegment.from_wav(input_path)
        trimmed_audio = audio[:30000]
        trimmed_audio.export(trimmed_path, format='wav')

        # Convert into spectrogram
        sample_rate, samples = wavfile.read(trimmed_path)
        frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

        # Plot spectrogram
        plt.figure(figsize=(10, 4))
        plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram + 1e-10), shading='gouraud')
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')

        destination = 'classical' # Change catagory for training data, else set as 'input'
        plt.savefig(f'spectrogram/{destination}/{filename}.png', dpi=300)
        continue
    else:
        print("non-wav audiofiles not supported")