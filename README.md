# ToneMaker

Travis L. Seymour, PhD

### A simple commandline tool to generate a sound files based on a pure tone specifications.

#### Args:

- frequency (int): The frequency of the tone in Hertz.
- duration (int): The duration of the sound in milliseconds.
- filename (str): The filename to save the sound file.

Note: The generated tone will be 16-bit with a 44100 sample rate.

ToneMaker is designed to run using PipX (https://github.com/pypa/pipx). See below for installation and use.

---

![screenshot.png](screenshot.png)

---

## Installing PipX


### ... Using A Package Manager

Instructions for installing on macOS, Linux, and Windows using a package manager can be found here: (https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx). 

All Linux distributions come with a built-in package manager, but users of macOS and Windows will need to install a package manager before installing PipX. On macOS this will require the Homebrew package manager (https://brew.sh/) and on Windows, this requires the Scoop  package manager (https://github.com/ScoopInstaller/Scoop). You will need to install the required package manager before following the instructions linked above.

### ... Using Python

If you'd rather not use a package manager to install PipX, you can do the following:

Make sure you have Python installed on your system. For macOS and Linux, it will be installed by default. On Windows, you can install Python via the app-store.

Open a terminal and issue these commands:

Install Pipx:

```bash
python -m pip install pipx
```

Make sure you can access installed apps directly from the commandline:

```bash
python -m pipx ensurepath
```

---

## Installing ToneMaker Using PipX

### You Installed PipX Using A Package Manager

Open a terminal and issue this command

```bash
pipx install "git+https://github.com/travisseymour/ToneMaker"
```

### You Installed PipX Using Python

Open a terminal and issue this command

```bash
python -m pipx install "git+https://github.com/travisseymour/ToneMaker"
```

--- 

## Using ToneMaker

To create a wavefile called "low_tone_220Hz.wav" that plays a 220 hertz tone for 100 milliseconds, enter a command like this:

```bash
tonemaker 220 100 low_tone_220Hz.wav
```

_if you have problems on MS Windows, see "Potential Issues On MS Windows" section below!_

---

## Upgrading ToneMaker Using PipX

If a new release of ToneMaker is posted on GitHub, you can upgrade your version using PipX.

### You Installed PipX Using A Package Manager

Open a terminal and issue this command

```bash
pipx upgrade tonemaker
```

### You Installed PipX Using Python

Open a terminal and issue this command

```bash
python -m pipx upgrade tonemaker
```

_if you have problems on MS Windows, see "Potential Issues On MS Windows" section below!_

---

## Potential Issues On MS Windows

### Windows can't locate PipX installed applications from the commandline

In some cases, the earlier `python -m pipx ensurepath` command won't correctly add the necessary folder to your sytem path. The result is that running PipX installed programs won't work properly. E.g., issuing commands like `tonemaker --help` will result in an error.

If you are in this situation, you can try manually adding the necessary PipX folder to your Windows PATH variable:

<mark>Make sure you type this command carefully and double-check it before pressing ENTER. Otherwise, you could leave your PATH in an unusable state.</mark>

```bash
setx PATH "%PATH%;C:\Users\YOURUSERNAME\.local\bin\"
```

Now close the terminal, re-open it, and try the command again.

---
