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

### --- Without Using A Package Manager

If you'd rather not use a package manager to install PipX, you can do the following:

- Make sure you have Python installed on your system. For macOS and Linux, it will be installed by default. On Windows, you can begin the installation by simply running `python` on the commandline. If it's not there, it will invite you to install it via the app-store.
- Go to the PipX releases page (https://github.com/pypa/pipx/releases) and download the latest version of `pipx.pyz`. Save this somewhere handy, because you will use it every time you interact with PipX. I recommend your home folder (e.g., `C:\Users\travis` on Windows, `/home/travis` on Linux and macOS) because it will be there whenever you open your terminal. Alternatively, you can put it wherever you want and add that location to your system Path variable.
- Once you have `pipx.pyz` in its final location, enter this command in the terminal: `python pipx.pyz ensurepath` and press ENTER. Now close and re-open the terminal.

---

## Installing ToneMaker Using PipX

### You Installed PipX Using A Package Manager

Open a terminal and issue this command

```bash
pipx install https://github.com/travisseymour/ToneMaker
```

### You Installed The ZipApp (pipx.pyz) Version of PipX

Open a terminal
 
If `pipx.pyz` is not somewhere on your Path, then navigate to the folder where `pipx.pyz` can be found

Now issue this command

```bash
python pipx.pyz install https://github.com/travisseymour/ToneMaker
```

--- 

## Using ToneMaker

### You Installed PipX Using A Package Manager

Open a terminal. 

To create a wavefile called "low_tone_220Hz.wav" that plays a 220 hertz tone for 100 milliseconds, enter a command like this:


```bash
tonemaker 220 100 low_tone_220Hz.wav
```

### You Installed The ZipApp (pipx.pyz) Version of PipX

Open a terminal

If `pipx.pyz` is not somewhere on your Path, then navigate to the folder where `pipx.pyz` can be found

To create a wavefile called "low_tone_220Hz.wav" that plays a 220 hertz tone for 100 milliseconds, enter a command like this:

```bash
python pipx.pyz run tonemaker 220 100 low_tone_220Hz.wav
```

---

## Upgrading ToneMaker Using PipX

If a new release of ToneMaker is posted on GitHub, you can upgrade your version using PipX

### You Installed PipX Using A Package Manager

Open a terminal and issue this command

```bash
pipx upgrade tonemaker
```

### You Installed The ZipApp (pipx.pyz) Version of PipX

Open a terminal
 
If `pipx.pyz` is not somewhere on your Path, then navigate to the folder where `pipx.pyz` can be found

Now issue this command

```bash
python pipx.pyz upgrade tonemaker
```

---
