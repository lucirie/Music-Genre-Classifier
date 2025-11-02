import matplotlib.pyplot as plt
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
        input_path = f'songs/{file}'
        output_path = 'tmp'
        audio = AudioSegment.from_wav(input_path)
        trimmed_audio = audio[0:30000]
        trimmed_audio.export(output_path, format='wav')

        # Convert into spectrogram
        sample_rate, samples = wavfile.read(f'{output_path}/{file}.wav')
        frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
        continue
    else:
        print("non-wav audiofiles not supported")