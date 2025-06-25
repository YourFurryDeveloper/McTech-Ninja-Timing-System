# Ninjaworks-Timing-System-Recreation
A cool recreation of the NinjaWorks timing and leaderboard system I made just for fun in 2 days while at Worlds!
____
<br />

## How to use it

If you know how to create a Python Flask webserver and how to deploy it, you probably know how to use this program lol, but I'm making a full-fledged tutorial for people who don't know how to do any of that.

### Table Of Contents
[How to install Python](#python-installation)

[Installing The Dependencies](#installing-the-dependencies-and-running-it)

[Configuring The System](#configuring-the-system)

____
____
<br />

### Python Installation

First, go to the [Python download page](https://python.org/downloads), and click the button that says `'Download Python X.XX.X'` (As of right now, it is 3.13.5.)

Once you have downloaded it, install it (obviously), and just use and follow all the default instructions and settings in the installer.
____
<br />

### Installing The Dependencies And Running It

Now that you have downloaded and installed Python, you will need to install the project and its dependencies.

First, click the green `Code` button located above the file container, and click `Download ZIP`.

Once you have the zip file downloaded, unzip it. (Double click the file on MacOS, and right click on the file and click `Extract All` on Windows.)

<br />
Now comes the 'hard' part for some of you (no offense, sorry 😭😭😭)

If you're on MacOS, click the command button and space bar (together) and type in `Terminal`. Open terminal.

If you're on Windows, press the Windows key and R (together) and type in `cmd`, then press enter.

<br />

Now, with Terminal/CMD open in the background, open Finder/File Explorer and find the unzipped folder with the files that you downloaded, but don't go into the folder. If you're on Windows, there may be a folder inside the folder, you want to use the one inside the folder for this next step.

Go back to Terminal and type cd and then a space, but don't press enter. Drag the folder of the project into Terminal, and now it should look something like `cd /path/to/the/folder/`. Press enter.

Once you have done that, type `pip install -r requirements.txt` into the terminal. This will install the dependencies needed to run the project.

When it's finished, all you have to do is type `python3 server.py`, and it should be all ready to go!
____
<br />

### Configuring The System
