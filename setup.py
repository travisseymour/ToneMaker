import os
from datetime import datetime
from pathlib import Path

from setuptools import find_packages, setup

PYTHON_VERSION = ">=3.9"

DEPENDENCIES = ["loguru", "numpy", "scipy", "typer"]

CURDIR = os.path.abspath(os.path.dirname(__file__))


def make_version():
    now = datetime.now()

    year = f"{str(now.year)[:5]}."
    month = f"{str(now.month).zfill(2)}."
    day = f"{str(now.day).zfill(2)}."
    minutes = str(now.hour * 60 + now.minute)

    date_string = f"{year}{month}{day}{minutes}"
    Path("statsview", "version.py").write_text(f'__version__ = "{date_string}"\n')
    return date_string


setup(
    name="tonemaker",
    version=make_version(),
    author="Travis L. Seymour, PhD",
    author_email="nogard@ucsc.edu",
    description="Tool for generating sound files based on a pure tone specifications.",
    long_description="Commandline application to generate sound files based on a pure tone specifications.",
    long_description_content_type="text/markdown",
    url="https://github.com/travisseymour/ToneMaker",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["tonemaker = tonemaker.__main__:app"],
    },
    install_requires=DEPENDENCIES,
    python_requires=PYTHON_VERSION,
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Utilities",
        "Topic :: Education",
    ],
)
