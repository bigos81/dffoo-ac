# Introduction
The software is designed to click through the UI of Dissidia Final Fantasy Opera to make an endless loop of a daily 
quest. I'm not aiming at code-for-everyone repo, that you just take and it works out of the box. It works for me an 
that's probably enough :)

# What do I use
## Game 
Opera Omnia at PlayStore: https://play.google.com/store/apps/details?id=com.square_enix.android_googleplay.DFFOperaOmnian&hl=en
Yes, i'm using Android. The game version i've tested this with is: 1.11.1.

## Screen Mirror / click software
Yep, the code works on PC, and the way I'm getting the video and am able to send clicks to the phone is thought
application called Vysor. You can download it from here: http://www.vysor.io/
I do use native client, but the chrome plug-in should work as well. I also do use **premium version**, so that the 
quality of the image is good. You may try with free version (which will pop-up ads as well) which you'll have to deal
with as well. Anyway my settings for video quality are:

- Bitrate: 2Mbit
- Resolution: 50%
- Decoder: Software

Depending on the phone you have (and it's resolution) you might want to tinker with those, or just set it as you want
and redo the images in res folder to match your graphics.

## Dependencies
I've copied a code from here: https://github.com/drov0/python-imagesearch. Read this guy's dependencies section to set
up your python environment with appropriate libs.

## How to use it
Ok so if you have everything in place:

- Start the game at your phone and:
    - Set up the team you want to grind experience with as you current team
    - Set Auto Battle on
    - Go to Missions -> Events -> Current crystal mission (the ones that cycle every day)
    - Make sure that the mission lvl70 is visible on screen
- Start Vysor and connect oto the phone
    - Make sure the Vysor window is on your **primary** display monitor (if you have multi monitor setup)
- Start the script
- Profit?

## Settings
Only settings are stored in global variables of the script:
```python
precision = 0.7
fail_in_a_row_threshold = 3
```
**precision** refers to image template matching precision (you'd have to dig deeper in openCV libs), 0.7 works for me

**fail_in_a_row_threshold** how many lost battles in the row terminates the script

## Known issues
The script will only work with Vysor being launched on primary screen monitor.

The scrip takes over control pf the mouse, so it's deigned to run on a machine you are not actively using. 

# End notes
Have fun with it :)

If you'd like to contact me you can do so via GitHub. 
If you found this software somewhere else than GitHub, then it sucks, original repo is here: https://github.com/bigos81/dffoo-ac
