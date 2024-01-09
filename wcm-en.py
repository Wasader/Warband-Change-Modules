import os
import time
import fnmatch

def welcome_message():
    print("""
    Welcome To,

    888       888       .d8888b.       888b     d888 
    888   o   888      d88P  Y88b      8888b   d8888 
    888  d8b  888      888    888      88888b.d88888 
    888 d888b 888      888             888Y88888P888 
    888d88888b888      888             888 Y888P 888 
    88888P Y88888      888    888      888  Y8P  888 
    8888P   Y8888      Y88b  d88P      888   "   888 
    888P     Y888       "Y8888P"       888       888
    """)

def change_module():
    os.system("clear")
    user = os.environ['USER']
    
    print("Searching for the directory where the game is installed. . .")
    steamdir = f"/home/{user}/.steam/debian-installation/steamapps/common/MountBlade Warband"
    steamdircontrol = os.path.isdir(steamdir)

    if not steamdircontrol:
        choice0 = input("Could not detect your game file, please specify the directory where the game is installed!")
        # Oyunu crack indirip dosya sistemini incele!
    else:
        gamefiledir = f"/home/{user}/.mbwarband"
        gamefilecontrol = os.path.isdir(gamefiledir)

        if not gamefilecontrol:
            print("The game's files containing config information could not be found. Please specify the directory!")
            # Crack... belki de başka bir hata var, bununla ilgili bilgilendirici bir yazı yazın!
        else:
            gmfilemodules = gamefiledir + "/last_module_warband"
            gmmainfile = steamdir + "/Modules/"

            print("The directory where the game is installed has been detected!")

            print("Available Modules!")
            modules = [name for name in os.listdir(gmmainfile) if os.path.isdir(os.path.join(gmmainfile, name))]

            a = 0
            for i in modules:
                a += 1
                print(a, i)

            allmod = len(modules)

            if allmod == 1:
                print("Only 1 mod detected in the Module Folder!")
                print("The current mod last_module_warband will be written to avoid possible errors!")

                changemodules = open(gmfilemodules, "w")
                changemodules.write(modules[0])
                print("The found mod has been successfully written!")
            else:
                try:
                    choice1 = int(input("Modules in the Modules folder. Please select. -->"))
                except ValueError:
                    print("Invalid Operation!")
                    return

                if choice1 > allmod or choice1 < 1:
                    os.system("clear")
                    print("Invalid Operation!")
                else:
                    changemodules = open(gmfilemodules, "w")
                    changemodules.write(modules[choice1 - 1])
                    changemodules.close()
                    os.system("clear")
                    print(f"Your game module set to {modules[choice1 - 1]}")
                    time.sleep(0.5)

def change_key():
    os.system("clear")
    user = os.environ['USER']

    print("Game Directories are controlling!")
    print("Searching for the directory where the game is installed. . .")
    steamdir = f"/home/{user}/.steam/debian-installation/steamapps/common/MountBlade Warband"
    steamdircontrol = os.path.isdir(steamdir)

    if not steamdircontrol:
        choice0 = input("Could not detect your game file, please specify the directory where the game is installed!")
        # Oyunu crack indirip dosya sistemini incele!
    else:
        gamefiledir = f"/home/{user}/.mbwarband"
        gamefilecontrol = os.path.isdir(gamefiledir)

        if not gamefilecontrol:
            print("The game's files containing config information could not be found. Please specify the directory!")
            # Crack... belki de başka bir hata var, bununla ilgili bilgilendirici bir yazı yazın!
        else:
            gmfilemodules = gamefiledir + "/last_module_warband"
            gmmainfile = steamdir + "/Modules/"

            print("The directory where the game is installed has been detected!")

            print("Key files are being scanned!")
            pattern = 'serial_key*'
            keylist = fnmatch.filter(os.listdir(gamefiledir), pattern)

            print("Which Mod would you like to change the key of?")
            a = 1
            for eleman in keylist:
                if eleman in "serial_key":
                    print(a, "- Native Key")
                elif eleman in "serial_key_nw":
                    print(a, "- Napoleonic Wars Key")
                a += 1

            allkey = len(keylist)

            try:
                choice2 = int(input("-->"))
            except ValueError:
                print("Invalid Operation!")
                return

            if choice2 > allkey or allkey < 1:
                print("Invalid Operation!")
            else:
                keyloc = gamefiledir + "/" + keylist[choice2 - 1]
                key = input("Enter Key -->")
                changekey = open(keyloc, "w")
                changekey.write(key)
                changekey.close()
                os.system("clear")
                print("The key was successfully changed. You are transferred to the main menu!")

def main():
    process = 0

    while process == 0:
        welcome_message()

        choice = input("""
        Select the action you want to do.
        1- Change Module
        2- Change Key
        3- Press Q to exit

        -->""")

        if choice.lower() == "q":
            break

        if choice == "1":
            process = 1
            change_module()
        elif choice == "2":
            process = 2
            change_key()
        else:
            process = 0
            os.system("clear")
            print("Invalid Operation!")
