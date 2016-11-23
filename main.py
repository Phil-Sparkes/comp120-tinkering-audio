import wave
import struct

noise_out = wave.open('noise2.wav', 'w')
soundWave = wave.open('noise99.wav', 'r')
# mode must be 'r', 'rb', 'w', or 'wb'

length = soundWave.getnframes()
frames = []

params = soundWave.getparams()
noise_out.setparams(params)



for i in xrange(length):
    waveData = soundWave.readframes(1)
    data = struct.unpack("<h", waveData)
    frames.append(int(data[0]))



def echo(sndFile, delay):
    values = []
    Channels = 1
    s1 = sndFile
    s2 = sndFile
    for index in range(delay, len(s1)):
        echo = 0.6*s2[index-delay]
        combo = s1[index] + echo
        s1[index] = combo
        packaged_value = struct.pack("<h", s1[index])
        for j in xrange(Channels):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)
    noise_out.close()
    return values

def double(source):
    values = []
    Channels = 2
    length = len(source) / 2 + 1
    target = [0] * length
    targetIndex = 0
    for sourceIndex in range(0, length, 2):
        value = source[sourceIndex]
        target[targetIndex] = value
        packaged_value = struct.pack("<h", target[targetIndex])
        targetIndex += 1
        for j in xrange(Channels):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)
    noise_out.close()
    return target

def half(source):
    values = []
    Channels = 2
    length = len(source)* 2
    target = [0] * length
    sourceIndex = 0
    for targetIndex in range(0, length):
        value = source[int(sourceIndex)]
        target[targetIndex] = value
        packaged_value = struct.pack("<h", target[targetIndex])
        sourceIndex = sourceIndex + 0.5
        for j in xrange(Channels):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)
    noise_out.close()
    return target

def increase_volume(frames, length):
    """Doubles the volume"""
    for i in xrange(length):
        frames[i] *= 2

def max():
    """finds the highest value"""
    maxnum = 0
    for i in xrange(length):
        challenger = frames[i]
        if abs(challenger) > maxnum:
            maxnum = abs(challenger)
    return maxnum

def count_sign_changes():
    """checks how many 0s"""
    numzero = 0
    for i in xrange(length):
        if frames[i] == 0:
            numzero += 1
    numzero = numzero/3    # 3 seconds
    numzero = numzero/2
    return numzero

BitDepth = 2**15 - 1
Volume = float(max()) / float(BitDepth)
#echo(frames, 300)
#double(frames)
half(frames)

#print frames
#print Volume
#print count_sign_changes()
#increase_volume(frames, length)


