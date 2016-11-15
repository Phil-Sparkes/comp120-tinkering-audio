import wave
import struct

soundWave = wave.open('noise2.wav', 'r')
# mode must be 'r', 'rb', 'w', or 'wb'

length = soundWave.getnframes()
frames = []

for i in xrange(length):
    waveData = soundWave.readframes(1)
    data = struct.unpack("<h", waveData)
    frames.append(int(data[0]))

print soundWave.getparams()

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



print frames

print max()
print count_sign_changes()
#increase_volume(frames, length)


