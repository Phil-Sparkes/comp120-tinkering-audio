import wave
import struct
import math

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

for i in xrange(Sample_Length):
    value = math.sin(2.0 * math.pi * Frequency * (i / 44100.0)) * (Volume * Bit_Depth)
    print value
    packaged_value = struct.pack("<h",value)

    for j in xrange(Channels):
        values.append(packaged_value)

value_str = ''.join(values)
noise_out.writeframes(value_str)

noise_out.close()
