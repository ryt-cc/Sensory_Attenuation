import array
import math

import pygame


def make_beep(frequency=440, duration_ms=500, volume=0.1):
    pygame.mixer.init(frequency=44100, size=-16, channels=1) # might wanna move this outside of this func at some point
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