"""
Copyright (c) 2024 Travis L. Seymour, PhD

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
import sys

import numpy as np
import typer
from scipy.io.wavfile import write

app = typer.Typer()


@app.command()
def generate_pure_tone(frequency: int, duration: int, filename: str):
    """
    Generate a sound file based on a pure tone specification.

    Args: frequency (int): The frequency of the tone in Hertz.
    duration (int): The duration of the sound in milliseconds.
    filename (str): The filename to save the sound file.

    E.g.:

    > tonemaker 220 100 low_tone_220Hz.wav
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

        msg = typer.style(f"Sound file '{filename}' generated successfully.", fg=typer.colors.GREEN)
        typer.echo(msg)

    except Exception as e:
        msg = typer.style(f"Generation of sound file '{filename}' failed: '{e}'", fg=typer.colors.RED)
        typer.echo(msg)


if __name__ == "__main__":
    app()
    sys.exit()
