#!/usr/bin/env python3

# almh (Arch Linux Maintenance Helper)
# (c) Voider 2020
# Contact me: voider (at) disroot dot org or as "invoider" at mastodon dot social
# https://invoider.wordpress.com
# License: FreeBSD(-like) License. Use at your own risk
# Gives you a CLI menu with some common maintenance options inside
# a *stock* Arch Linux system
# Plausibly works on derivatives too, but not tested at the moment.
# Pacman is absolutely needed, pacman-contrib and newsboat are needed for some options.
# Please read the README file and code before using this
green = "\033[32m"
cyan = "\033[36m"
red = "\033[31m"
blue = "\033[34m"
resetc = "\33[m"
commands = ['"newsboat -r"', '"sudo pacman -Syu"', '"sudo paccache -rk3 -v"', '"pacman -Ss "+input("Type the package name or keyword of the package you want to query: ")', '"sudo pacman -S "+input("Type the package name(s) you want to install: ")', '"sudo pacman -Rs "+input("Type the name of the package(s) you want to remove from your system: ")', '"sudo paccache -ruk0 -v"', '"sudo pacman -Qtdq | sudo pacman -Rns -"', '"pacman -Qe | column"', '"pacman -Q | column"', '', '"sudo pacman -S pacman-contrib"', '"sudo pacman -S newsboat && sleep 4 && mkdir ~/.config/newsboat/ && echo https://archlinux.org/feeds/news/ > ~/.config/newsboat/urls"']
print("\n" , red + "IMPORTANT.", resetc + "If you are using this for the first time, you'll need")
print ("newsboat and pacman-contrib to use options 1, 3 and 7 .")
print('Type special option' , green + "'12'" , resetc + 'to install pacman-contrib.')
print('Type special option' , green + "'13'" , resetc + "to install newsboat and add Arch news RSS")
print('to read the Arch web news section before upgrading.\n')
print(blue + '************************************************************************' , resetc)
print(blue + '**' , resetc , '                            almh                                 ' , blue + '**' , resetc)
print(blue + '**' , resetc , '                (ARCH LINUX MAINTENANCE HELPER)                  ' , blue + '**' , resetc)
print(blue + '************************************************************************' , resetc)
print('\n')
print("PLEASE CHOOSE AN OPTION (type a number 1-11):\n***Entries marked with '#' will run with sudo.\nWrite your password if, and when, prompted***\n")
import os
while True:
    try:
        print(cyan + """************************************************************************
* 1.  Read the Arch web news section before upgrading your system      *
* 2.  # Update and upgrade your system                                 *
* 3.  # Remove all cached versions of installed and uninstalled        *
*      packages (except for the most recent 3 versions)                *
* 4.  Search packages in the repositories database                     *
* 5.  # Install packages                                               *
* 6.  # Remove installed package(s) (with unneeded dependencies)       *
* 7.  # Remove all cached versions of uninstalled packages             *
* 8.  # Remove orphaned packages                                       *
* 9.  List explicitly installed packages                               *
* 10. List all installed packages                                      *
* 11. Exit                                                             *
************************************************************************\n
 """ , resetc)
        options = int(input())-1
        commands_arr = list(range(len(commands)))
        print(options)
        print(commands_arr[:10] + commands_arr[11:])
        if options in commands_arr[:10] + commands_arr[11:]:
            exec("os.system("+commands[options]+")")
            print("\n")
        elif options == 10:
            print("Thank you for using almh")
            break
        else:
            print(red + "Please choose an option, 1-11\n" , resetc)
    except KeyboardInterrupt:
        exit()
    except:
        print(red + "Please choose an option, 1-11\n" , resetc)
