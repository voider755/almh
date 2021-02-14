# almh
# (Arch Linux Maintenance Helper)
![alt text](https://raw.githubusercontent.com/voider755/almh/main/Screenshot_2020-12-28_10-25-09.png)

Gives you a CLI menu with some common maintenance options inside an Arch Linux system 

The Python code is basically a "wrapper" to execute ```pacman```/```paccache```/```newsboat``` commands. They're all, I believe, fairly "safe" (as "safe" as they would be executed outside of ```almh```, that is), non-agressive common maintenance options, all of them rightfully documented in the Arch Wiki. It is advised to review the Arch Linux web before running a system update/upgrade, to check for possible required manual interventions and whatnot, so an "extra" option to install ```newsboat``` and add the Arch web news RSS is added. After this, you can check for Arch news with a ```newsboat``` option inside the ```almh``` menu. Another "extra" option should install ```pacman-contrib```, which is not present in a "base" Arch Linux installation.

AUR helpers are not currently supported, but the code can easily be forked to switch ```pacman``` commands for, say, ```yay``` ones.

DISCLAIMER: Check the operations executed by ```almh``` code before performing any operation with this and be sure of what they do and if you want to use them. USE AT YOUR OWN RISK.

INSTALLATION: It's [in the AUR](https://aur.archlinux.org/packages/almh-git/) as ```almh-git``` (thanks to lxgr!), so you can install it from there. Follow the Arch wiki directions for installing from the AUR, or use your AUR helper of choice. You just need Python (it works with the current version inside Arch official repositories), ```sudo``` (or a ```sudo``` compatible alternative), a terminal emulator if in a graphic session and, of course, an Arch Linux (may or may not work as expected in a derivative) system installed. The optional dependencies ```newsboat``` and ```pacman-contrib``` can be installed (with the Arch news RSS automatically added in ```newsboat```) afterwards using ```almh```. After installation, you can launch the application from the command line with ```almh.py```. You can write a ```$SHELL``` alias if you want to remove the ```.py``` from the launch command. Say you use ```bash```, then in ```.bashrc```

```alias almh='almh.py'```


In case you don't want to use the AUR package, you can download ```almh.py``` from here. To install it, move it to your ```$PATH``` and give it appropiate permissions to run if necessary. If you prefer to keep it outside of your ```$PATH``` (likely, somewhere inside your ```$HOME```), you won't need to make the archive executable. Just open your terminal emulator, navigate to the directory where the archive is contained, and type:

```shell
$ ./almh.py
```
Or use full path from elsewhere.

You may want to add an alias to your ```$SHELL```, like this:
```shell
alias almh='/full_path_to_the_archive/almh.py'
```
Then just type ```almh``` (or whatever alias you prefer to use), and it should run.
****************************************************************************
CHANGES: 
- File made executable without the Python prefix and added option to exit the program with ```Ctrl+c``` (thanks xgr-linux!)
- Now, after performing a package query, an option to ask if the user wants to install some package pops up automatically.
- The shell script which installs ```newsboat``` won't overwrite any (likely non existent) ```urls``` config file. Plus, it is now put inside the more XDG-compliant ```~/.config/newsboat``` instead of the app default ```~/.newsboat``` (thanks u/TopDownTom, u/MuddyArch and u/armoredkitten22 from the Arch Linux Reddit community for their explanations and suggestions!)
- (Update 02/14/21) New option to check ```.pac*``` files using ```pacdiff``` (which is part of ```pacman-contrib```). Internally it uses ```vimdiff```, so you can use ```vim``` commands to manage this. Please check [this entry in the Arch Wiki](https://wiki.archlinux.org/index.php/Vim#Merging_files). (This and some more, thanks again to xgr-linux!)

TO DO:
- "Prettify" the scheme a bit.
- Add a submenu with some "advanced" options.
- Remove the ".py" in the executable file name.
****************************************************************************
almh (Arch Linux Maintenance Helper) is (c) Voider 2020
Contact me: voider (at) disroot.org or as "invoider" at mastodon dot social
License: FreeBSD(-like) License. Use at your own risk

Arch Linux Copyright © 2002-2020 Judd Vinet, Aaron Griffin and Levente Polyák.
The Arch Linux name and logo are recognized trademarks. Some rights reserved.
Linux(R) is a registered trademark of Linus Torvalds
This project is totally independent and in no way affiliated with Arch Linux (c) and/or Linux(R)
