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

def sineWave(freq, amplitude, length):
    values = []
    buildSin = [0] * (length)
    samplingRate = length
    interval = 1.0 / freq
    samplesPerCycle = interval * samplingRate
    maxCycle = 2 * math.pi
    for pos in range (len(buildSin)):
        rawSample = math.sin((pos / samplesPerCycle) * maxCycle)
        sampleVal = int(amplitude * rawSample)
        packaged_value = struct.pack("<h", sampleVal)

        for j in xrange(Channels):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)
    return buildSin
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
for x in xrange(9):
    choice = random.randint(0,3)
    if choice == 1:
        sineWave(440, 2000, 44100)
    elif choice == 2:
        sineWave(880, 4000, 44100)
    elif choice ==3:
        sineWave(1320, 8000, 44100)

