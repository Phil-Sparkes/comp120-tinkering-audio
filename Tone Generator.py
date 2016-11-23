import wave
import struct
import math
import random
noise_out = wave.open('noise.wav', 'w')

noise_out.setnchannels(1)
noise_out.setsampwidth(2)
noise_out.setframerate(44100)
noise_out.setnframes(44100)
noise_out.setcomptype('NONE', 'not compressed')

values = []

print noise_out.getparams()

Sample_Length = noise_out.getframerate()
Channels = noise_out.getnchannels()
print Channels
Frequency = 2000
Sample_Rate = Sample_Length
Volume = 0.5
Bit_Depth = 2**15 - 1

def sineWave(frequency, volume, attack_time, sustain_time, release_time):
    values = []
    volumechange = 0.00
    buildSin = [0] * (attack_time + sustain_time + release_time)
    samplingRate = 44100
    interval = 1.0 / frequency
    samplesPerCycle = interval * samplingRate
    maxCycle = 2 * math.pi

    for pos in range(attack_time):
        volumechange += (float(volume) / float(attack_time))
        rawSample = math.sin((pos / samplesPerCycle) * maxCycle)
        sampleVal = int(volumechange * rawSample)
        packaged_value = struct.pack("<h", sampleVal)
        for j in xrange(Channels):
            values.append(packaged_value)
    for pos in range(sustain_time):
        rawSample = math.sin((pos / samplesPerCycle) * maxCycle)
        sampleVal = int(volumechange * rawSample)
        packaged_value = struct.pack("<h", sampleVal)
        for j in xrange(Channels):
            values.append(packaged_value)
    volumechange = 0
    for pos in range(release_time):
        volumechange += (float(volume) / float(release_time))
        rawSample = math.sin((pos / samplesPerCycle) * maxCycle)
        sampleVal = ((int(volume-volumechange)) * rawSample)
        packaged_value = struct.pack("<h", sampleVal)
        for j in xrange(Channels):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)
    return buildSin

notes = {'a': 440.0 * 2.0 ** (0 / 12.0),
        'a#': 440.0 * 2.0 ** (1 / 12.0),
        'b': 440.0 * 2.0 ** (2 / 12.0),
        'c': 440.0 * 2.0 ** (3 / 12.0),
        'c#': 440.0 * 2.0 ** (4 / 12.0),
        'd': 440.0 * 2.0 ** (5 / 12.0),
        'd#': 440.0 * 2.0 ** (6 / 12.0),
        'e': 440.0 * 2.0 ** (7 / 12.0),
        'f': 440.0 * 2.0 ** (8 / 12.0),
        'f#': 440.0 * 2.0 ** (9 / 12.0),
        'g': 440.0 * 2.0 ** (10 / 12.0),
        'g#': 440.0 * 2.0 ** (11 / 12.0)}


attacktime = int(0.1 * 44100)
sustaintime = int(0.6 * 44100)
decaytime = int(0.3 * 44100)
volumenote = 8000

playnotes = ['c','c','g','g','a','a','g','f','f','e','e','d','d','c','g','g','f','f','e','e','d','g','g','f','f','e','e','d']
freqnote = 440.0 * 2.0 ** (notes['g'] / 12.0)

for note in range(len(playnotes)):
    sineWave(notes[playnotes[note]], volumenote, attacktime, sustaintime, decaytime)



"""
for i in xrange(Sample_Length):
    value = math.sin(2.0 * math.pi * Frequency * (i / 44100.0)) * (Volume * Bit_Depth)
    print value
    packaged_value = struct.pack("<h",value)

    for j in xrange(Channels):
        values.append(packaged_value)

value_str = ''.join(values)
noise_out.writeframes(value_str)

noise_out.close()

"""