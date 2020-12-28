#!/usr/bin/env python3
# almh (Arch Linux Maintenance Helper)
# (c) Voider 2020
# Contact me: voider (at) disroot dot org or as "invoider" at mastodon dot social
# https://invoider.wordpress.com
# License: FreeBSD(-like) License. Use at your own risk
# Gives you a CLI menu with some common maintenance options inside 
# a *stock* Arch Linux system
# Please read the README file and code before using this
green = '\033[32m'
cyan = '\033[36m'
red = '\033[31m'
blue = '\033[34m'
resetc = '\33[m'
print('\n' , red + 'IMPORTANT.', resetc + "If you are using this for the first time, you'll need")
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
* 6   # Remove installed package(s) (with unneeded dependencies)       *
* 7.  # Remove all cached versions of uninstalled packages             *
* 8.  # Remove orphaned packages                                       *
* 9.  List explicitly installed packages                               *
* 10. List all installed packages                                      *
* 11. Exit (type 11 or use Ctrl+c)                                     *
************************************************************************\n
 """ , resetc)
        options = int(input())
        if options == 1:
            os.system("newsboat -r")
        elif options == 2:
            os.system("sudo pacman -Syu")
            print("\n")
        elif options == 3:
            os.system("sudo paccache -rk3 -v")
            print("\n")
        elif options == 4:
            package = input('Type the package name or keyword of the package you want to query: ')
            os.system('pacman -Ss ' + package)
            print("\n")
            pkginstall = str(input("Do you want to install any package? (type 'y', anything else to continue) "))
            if pkginstall == 'y':
                install = input('Type the package name(s) you want to install: ')
                os.system('sudo pacman -S ' + install)
            elif pkginstall != 'y':
                continue
        elif options == 5:
            install = input('Type the package name(s) you want to install: ')
            os.system('sudo pacman -S ' + install)
            print('\n')
        elif options == 6:
            remove = input('Type the name of the package(s) you want to remove from your system: ')
            os.system('sudo pacman -Rs ' + remove)
            print("\n")
        elif options == 7:
            os.system("sudo paccache -ruk0 -v")
            print("\n")
        elif options == 8:
            os.system('sudo pacman -Qtdq | sudo pacman -Rns -')
            print("\n")
        elif options == 9:
            os.system('pacman -Qe | column')
            print("\n")
        elif options == 10:
            os.system('pacman -Q | column')
            print("\n")
        elif options == 12:
            os.system('sudo pacman -S pacman-contrib')
            print("\n")
        elif options == 13:
            os.system("sudo pacman -S newsboat && sleep 4 && mkdir ~/.config/newsboat/ && echo 'https://archlinux.org/feeds/news/' >> ~/.config/newsboat/urls")
            print("\n")
        elif options == 11:
            print("Thank you for using almh")
            break
        else:
            print(red + "Please choose an option, 1-11\n" , resetc)
    except KeyboardInterrupt:
        exit()
    except:
        print (red + "Please choose an option, 1-11\n" , resetc)

