import array
import math
import time
import pygame


def make_beep(frequency=440, duration_ms=500, volume=0.1):
    pygame.mixer.init(frequency=44100, size=-16, channels=1)
    sample_rate = 44100
    n_samples = int(sample_rate * (duration_ms / 1000.0))
    amplitude = int(32767 * volume)

    # Generate a sine wave
    buf = array.array(
        "h",
        [
            int(amplitude * math.sin(2.0 * math.pi * frequency * i / sample_rate))
            for i in range(n_samples)
        ],
    )
    return pygame.mixer.Sound(buffer=buf)


# Create and play a 440 Hz beep for 0.5 seconds
beep = make_beep(frequency=440, duration_ms=500)
beep.play()

# Keep the script alive long enough to hear the sound
time.sleep(0.5)
