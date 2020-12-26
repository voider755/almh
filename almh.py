# almh (Arch Linux Maintenance Helper)
# (c) Voider 2020
# Contact me: voider (at) disroot dot org or as "invoider" at mastodon dot social
# https://invoider.wordpress.com
# License: FreeBSD License. Use at your own risk
# Gives you a menu with some common maintenance options inside a *stock* Arch Linux system
# Plausibly works on derivatives too, but not tested at the moment. 
# Pacman is absolutely needed, pacman-contrib is needed for some options.
# Please read the README file and code before using this 
green = '\033[32m'
cyan = '\033[36m'
red = '\033[31m'
resetc = '\33[m'
print(green + '************************************************************************' , resetc)
print(green + '**' , resetc , '                            almh                                 ' , green + '**' , resetc)
print(green + '**' , resetc , '                (ARCH LINUX MAINTENANCE HELPER)                  ' , green + '**' , resetc)
print(green + '************************************************************************' , resetc)
print('\n')
print("PLEASE CHOOSE AN OPTION (type a number 1-13):\n***Options xx require that you have pacman-contrib installed.\nEntries marked with '#' will run with sudo.\nWrite your password if, and when, prompted***\n")
import os
while True:
    try:
        print(cyan + """************************************************************************
* 1.  # Update and upgrade your system                                 *
* 2.  # Update and upgrade your system (verbose mode)                  *
* 3.  # Clean downloaded packages cache                                *
* 4.  # Remove orphaned packages                                       *
* 5.  Search packages in the repositories database                     *
* 6.  # Install packages                                               *
* 7   # Remove installed package(s) (with unneeded dependencies)       *
* 8.  List all installed packages                                      *
* 9.  List explicitly installed packages                               *
* 10. Remove all cached versions of installed and uninstalled packages *
      (Except for the most recent 3 versions)                          *
* 11. # Remove all cached versions of uninstalled packages             *
* 12. # Remove ALL old kernels (exits if no old kernels are found)     *
* 13. Exit                                                             *
************************************************************************\n
 """ , resetc)
        options = int(input())
        if options == 1:
            os.system("sudo pacman -Syu")
            print("\n")
        elif options == 2:
            os.system("sudo xbps-install -Suv")
            print("\n")
        elif options == 3:
            os.system("sudo xbps-remove -Ov")
            print("\n")
        elif options == 4:
            os.system("sudo xbps-remove -ov")
            print("\n")
        elif options == 5:
            package = input('Type the package name or keyword of the package you want to query: ')
            os.system('pacman -Ss ' + package)
            print("\n")
        elif options == 6:
            install = input('Type the package name(s) you want to install: ')
            os.system('sudo pacman -S ' + install)
            print('\n')
        elif options == 7:
            remove = input('Type the name of the package(s) you want to remove from your system: ')
            os.system('sudo pacman -Rs ' + remove)
            print("\n")
        elif options == 8:
            os.system("pacman -Ql")
            print("\n")
        elif options == 9:
            os.system("pacman -Qe | column")
            print("\n")
        elif options == 10:
            #print("You can remove this/these old kernel versions:\n(Empty if no old kernels are found)")
            os.system("sudo paccache -rv")
            print("\n")
        elif options == 11:
			os.system("sudo paccache -ruk0 -v")
            #vkpurge = input("Type the kernel version you want to remove:\n(Use option 10 before, type anything to exit back to menu) ")
            #os.system("sudo vkpurge rm " + vkpurge)
            print("\n")
        elif options == 12:
            os.system("sudo vkpurge rm all")
            print("\n")
        elif options == 13:
            print("Thank you for using vlmh")
            break
        else:
            print(red + "Please choose an option, 1-13\n" , resetc)
    except:
        print (red + "Please choose an option, 1-13\n" , resetc)

