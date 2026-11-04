"""
Copyright (c) 2024-2026 Travis L. Seymour, PhD

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import cyclopts
import numpy as np
from scipy.io.wavfile import write

app = cyclopts.App(
    help="Tool for generating sound files based on pure tone specifications."
)


@app.default
def generate_pure_tone(frequency: int, duration: int, filename: str):
    """
    Generate a sound file based on a pure tone specification.

    Args:
        frequency: The frequency of the tone in Hertz.
        duration: The duration of the sound in milliseconds.
        filename: The filename to save the sound file.

    Example:
        tonemaker 220 100 low_tone_220Hz.wav
    """

    try:
        # sample calc
        duration_sec = duration / 1000.0
        sample_rate = 44100
        num_samples = int(sample_rate * duration_sec)

        # init wave data container
        t = np.linspace(0, duration_sec, num_samples)

        # Generate the waveform for the pure tone
        data = np.sin(2 * np.pi * frequency * t)
        scaled_data = np.int16(data * 32767)

        # save to wave container
        # TODO: see if it's possible to have an option for mp3 files
        write(filename, sample_rate, scaled_data)

        print(f"\033[32mSound file '{filename}' generated successfully.\033[0m")

    except (ValueError, OSError) as e:
        print(f"\033[31mGeneration of sound file '{filename}' failed: '{e}'\033[0m")


def main():
    app()


if __name__ == "__main__":
    main()
