import wave
import struct
import math

# Creates a file to write to
noise_out = wave.open('noise.wav', 'w')

# Creates the parameters of the file
noise_out.setnchannels(1)
noise_out.setsampwidth(2)
noise_out.setframerate(44100)
noise_out.setnframes(44100)
noise_out.setcomptype('NONE', 'not compressed')
Channels = noise_out.getnchannels()


def sine_wave(frequency, volume, attack_time, sustain_time, release_time):
    """Envelope function, plays a pure tone but fades into and out of it"""
    # Creates volume_change as a float
    volume_change = 0.00

    # Creates a list for storing all the values
    values = []

    # Sets the sampling rate
    sampling_rate = 44100

    # creates an interval between samples
    interval = 1.0 / frequency
    samples_per_cycle = interval * sampling_rate

    # not sure what that one does
    max_cycle = 2 * math.pi

    # loops for length of the pure tone
    for pos in range((attack_time + sustain_time + release_time)):
        # Increases the volume from 0 when in attack time
        if attack_time >= pos:
            volume_change += (float(volume) / float(attack_time))
        # Decreases the volume to 0 when in decay time
        if (attack_time + sustain_time) <= pos:
            volume_change -= (float(volume) / float(release_time))

        # Creates the sample
        raw_sample = math.sin((pos / samples_per_cycle) * max_cycle)
        sample_value = int(volume_change * raw_sample)

        # Packages the and appends the sample
        packaged_value = struct.pack("<h", sample_value)
        for j in xrange(Channels):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)

# Dictionary of notes
notes = {
    'a': 440.0 * 2.0 ** (0 / 12.0),
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
    'g#': 440.0 * 2.0 ** (11 / 12.0),
    'a2': 440.0 * 2.0 ** (12 / 12.0)
}

# Sets the length of the note in seconds
note_time = 0.4
# sets the percentage of the notes attack, sustain and decay times, values add up to 1
attacktime = int((0.1 * note_time) * 44100)
sustaintime = int((0.6 * note_time) * 44100)
decaytime = int((0.3 * note_time) * 44100)

# sets the volume
volumenote = 8000

# Twinkle Twikle in list form
playnotes = ['c', 'c', 'g', 'g', 'a2', 'a2', 'g', 'f', 'f', 'e', 'e', 'd', 'd', 'c', 'g', 'g', 'f', 'f', 'e', 'e', 'd', 'g', 'g', 'f', 'f', 'e', 'e', 'd']

# creates the notes
for note in range(len(playnotes)):
    sine_wave(notes[playnotes[note]], volumenote, attacktime, sustaintime, decaytime)

    # this part is for random notes and random times played for can uncomment if want to try
    """
    note_time = random.choice([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    attacktime = int((0.1 * note_time) * 44100)
    sustaintime = int((0.6 * note_time) * 44100)
    decaytime = int((0.3 * note_time) * 44100)
    sine_wave(notes[random.choice(['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e','f', 'f#', 'g', 'g#'])], volumenote, attacktime, sustaintime, decaytime)
    """
