# almh
# (Arch Linux Maintenance Helper)
![alt text](https://raw.githubusercontent.com/voider755/almh/main/Screenshot_2020-12-28_10-25-09.png)

Gives you a CLI menu with some common maintenance options inside an Arch Linux system 

The Python code is basically a "wrapper" to execute pacman/paccache/newsboat commands. They're all, I believe, fairly "safe", non-agressive common maintenance options,all of them rightfully documented in the Arch Wiki. It is advised to review the Arch Linux web before running a system update/upgrade, to check for possible required manual interventions and whatnot, so an "extra" option to install newsboat and add the Arch web news RSS is added. After this, you can check for Arch news with a newsboat option inside the almh menu. Another "extra" option should install pacman-contrib, which is not present in a "base" Arch Linux installation.

AUR helpers are not currently supported, but the code can easily be forked to switch pacman commands for, say, yay ones.

DISCLAIMER: This is an alpha release. I'm no coder, just trying to learn some Python and did this as a learning experience. I'm releasing this because a) it seems to work, and I think someone may find it useful, and more important b) because someone may check the code, point where it's wrong, and help me improve it. You can of course check the almh code before performing any operation with this. USE AT YOUR OWN RISK.

INSTALLATION: I don't think there's really a need to install it. You just need Python (it works with the current version inside Arch official repositories), a terminal emulator if in a graphic session and, of course, an Arch Linux (may or may not work as expected in a derivative) system installed. If it's outside of $PATH, just open your terminal emulator, navigate to the directory where the archive is contained, and type:

$ ./almh.py

Or use full path from elsewhere.

You can of course add an alias to your $SHELL, say you use bash, then in .bashrc:

alias almh='/full_path_to_the_archive/almh.py'

Then just type almh (or whatever alias you prefer to use), an it should run.
****************************************************************************
CHANGES: 
- File made executable without the Python prefix and added option to exit the program with Ctrl+c (thanks xgr-linux!)
- Now, after performing a package query, an option to ask if the user wants to install some package pops up automatically.
- The shell script which install newsboat won't overwrite any (likely non existent) urls config file. Plus, it is now put inside the more XDG-compliant ~/.config/newsboat instead of the app default ~/.newsboat (thanks u/TopDownTom, u/MuddyArch and u/armoredkitten from the Arch Linux Reddit community for their explanations and suggestions!)
****************************************************************************
almh (Arch Linux Maintenance Helper) is (c) Voider 2020
Contact me: voider (at) disroot.org or as "invoider" at mastodon dot social
License: FreeBSD(-like) License. Use at your own risk

Arch Linux Copyright © 2002-2020 Judd Vinet, Aaron Griffin and Levente Polyák.
The Arch Linux name and logo are recognized trademarks. Some rights reserved.
Linux(R) is a registered trademark of Linus Torvalds
This project is totally independent and in no way affiliated with Arch Linux (c) and/or Linux(R)
