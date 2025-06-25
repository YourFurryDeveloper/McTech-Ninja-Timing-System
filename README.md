# McTech Ninja Timing System
A cool recreation of the ninja timing and leaderboard system I made just for fun in 2 days while at Worlds!
____
<br />

## How to use it

If you know how to create a Python Flask webserver and how to deploy it, you probably know how to use this program lol, but I'm making a full-fledged tutorial for people who don't know how to do any of that.

### Table Of Contents
[How to install Python](#python-installation)

[Installing The Dependencies](#installing-the-dependencies-and-running-it)

[Configuring The System](#configuring-the-system)

[How To Control It and Use the Leaderboard](#how-to-control-it-and-use-the-leaderboard)

[Gallery](#gallery)
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

When you run it, you will see an output like this:

```
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 *Running on all addresses (0.0.0.0)
 *Running on http://127.0.0.1:5000
 *Running on http://10.0.0.150:5000
```

Where it says `Running on http://10.0.0.150:5000`, you will see something other than `10.0.0.150`. This is the address of the timing system. Open that URL in a browser on any device (preferably a computer). You will see the leaderboard!

To configure it though, go to that URL and add /config to it. You will see a configuration screen.

Fill out all the text boxes with the name of the competition, the division, and the name of the course. Once you have done that, select the course type.

Once this is finished, scroll down to where it says Obstacles and click `Add obstacle`. Add all the obstacles in the course in the order that you want them to be run.

Go down to the Competitors section, and repeat the same process as adding obstacles, but instead, fill out the competitor's info. The order you add them is the run order.

Once you are finished, click the button at the top of the page that says `Push and save all configs`, and a popup will appear. It will dissappear once everything has been saved.

Congratulations! You are ready to run the course!
____
<br />

### How To Control It and Use the Leaderboard

Here is a list of all the URLS that the system has. (append these to the end of the URL you got from the command output.)

* / (This is the main leaderboard, you can open this on a computer or TV for the best viewing experience.)
* /controller (This is the endpoint that you will open on a phone to control the system.)
* /config (The page you just used to configure the system.)
* /timer (Open this on another device if you want, this is the actual timer display, like the ones that hang from the rigs at Worlds.)
* /buzzer (I highly reccomend opening this on a second phone and setting it where the finish will be. It is literally just a big red buzzer button.)

On the /controller page, you will see 6 buttons.
* Fail
* Finish (To manually finish if you aren't using /buzzer on another device at the end of the course.)
* Start (Starts the timer with NO COUNTDOWN)
* Obstacle (Press this when the runner completes an obstacle.)
* Pause (Pauses the timer)
* Resume (Resumes the timer

<br />

At the beginning of the course, press start. This will start the timer with no countdown.

When the competitor completes an obstacle, press obstacle.

To pause and resume the time, use those buttons.

If you aren't using a second phone as the buzzer, then just press finish when the runner completes the course or fail if they fall or fail to complete it depending on what kind of course you are doing. If they run out of time, they will automatically be failed.
____
____
<br />

## Gallery
