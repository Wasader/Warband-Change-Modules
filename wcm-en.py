import os
import time
import fnmatch

def welcome_message():
    print("""
    Welcome,

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
    
    print("Searching for the Directory where the Game is Installed. . .")
    steamdir = f"/home/{user}/.steam/debian-installation/steamapps/common/MountBlade Warband"
    steamdircontrol = os.path.isdir(steamdir)

    if not steamdircontrol:
        choice0 = input("The game directory could not be detected, please specify the directory where the game is installed!")
        # Download and inspect the cracked version of the game file system!
    else:
        gamefiledir = f"/home/{user}/.mbwarband"
        gamefilecontrol = os.path.isdir(gamefiledir)

        if not gamefilecontrol:
            print("The files containing the game's config information could not be found. Please specify the directory!")
            # Crack... maybe there is another error, write an informative message about it!
        else:
            gmfilemodules = gamefiledir + "/last_module_warband"
            gmmainfile = steamdir + "/Modules/"

            print("The directory where the game is installed has been detected!")

            print("Current Modules!")
            modules = [name for name in os.listdir(gmmainfile) if os.path.isdir(os.path.join(gmmainfile, name))]

            a = 0
            for i in modules:
                a += 1
                print(a, i)

            allmod = len(modules)

            if allmod == 1:
                print("Only 1 module detected in the Module Folder!")
                print("To prevent possible errors, the current module will be set as last_module_warband!")

                changemodules = open(gmfilemodules, "w")
                changemodules.write(modules[0])
                print("The found module has been successfully written!")
            else:
                try:
                    choice1 = int(input("Modules found in the folder. Please make a selection. -->"))
                except ValueError:
                    print("Invalid Operation!")
                    return

                if choice1 > allmod or choice1 < 1:
                    print("Invalid Operation!")
                else:
                    changemodules = open(gmfilemodules, "w")
                    changemodules.write(modules[choice1 - 1])
                    changemodules.close()
                    os.system("clear")
                    print(f"Your game is set to the module {modules[choice1 - 1]}")
                    time.sleep(0.5)

def change_key():
    os.system("clear")
    user = os.environ['USER']

    print("Checking Game Directories!")
    print("Searching for the Directory where the Game is Installed. . .")
    steamdir = f"/home/{user}/.steam/debian-installation/steamapps/common/MountBlade Warband"
    steamdircontrol = os.path.isdir(steamdir)

    if not steamdircontrol:
        choice0 = input("The game directory could not be detected, please specify the directory where the game is installed!")
        # Download and inspect the cracked version of the game file system!
    else:
        gamefiledir = f"/home/{user}/.mbwarband"
        gamefilecontrol = os.path.isdir(gamefiledir)

        if not gamefilecontrol:
            print("The files containing the game's config information could not be found. Please specify the directory!")
            # Crack... maybe there is another error, write an informative message about it!
        else:
            gmfilemodules = gamefiledir + "/last_module_warband"
            gmmainfile = steamdir + "/Modules/"

            print("The directory where the game is installed has been detected!")

            print("Scanning Key files!")
            pattern = 'serial_key*'
            keylist = fnmatch.filter(os.listdir(gamefiledir), pattern)

            print("Which Module's key do you want to change?")
            a = 1
            for element in keylist:
                if element in "serial_key":
                    print(a, "- Native Key")
                elif element in "serial_key_nw":
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
                key = input("Enter the Key -->")
                changekey = open(keyloc, "w")
                changekey.write(key)
                changekey.close()
                os.system("clear")
                print("Key successfully changed. You are being transferred to the main menu!")

def main():
    process = 0

    while process == 0:
        welcome_message()

        choice = input("""
        Please select the operation you want to perform.
        1- Change Module
        2- Change Key
        3- Press Q to Quit

        -->""")

        if choice.lower() == "q":
            break

        if choice == "1":
            process = 1
            change_module()
        elif choice == "2":
            process = 2

