import os
import time
import fnmatch
process = 0

while process == 0:
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

 choice = input("""Select the action you want to do.
 1-Change Module
 2-Change Key
 3-Press Q to exit

 -->""")
 if choice == "q":
  break
 elif choice == "Q":
  break
 process = 1
 while process == 1:
    #Seçim 1
    if choice == "1":
        os.system("clear")
        user = os.environ['USER']
        print("Searching for the directory where the game is installed . . .")
        steamdir = "/home/"+user+"/.steam/debian-installation/steamapps/common/MountBlade Warband"
        steamdircontrol = os.path.isdir(steamdir)
        if steamdircontrol == False:
          choice0 = input("Could not detect your game file, please specify the directory where the game is installed!")
          #Oyunu crack indirip dosya sistemini incele!
        else:
          gamefiledir = "/home/"+user+"/.mbwarband"
          gamefilecontrol = os.path.isdir(gamefiledir)
          if gamefilecontrol == False:
            print("The game's files containing config information could not be found. Please specify the directory!")
            #Crack... belkide başka hata kim bilebilir bunla ilgili bilgilendirici yazı yaz!
          gmfilemodules = gamefiledir+"/last_module_warband"
          gmmainfile = steamdir+"/Modules/"
        print("The directory where the game is installed has been detected!")
        process = 2
        while process == 2:
          if steamdircontrol == True:
            print("Available Modules!")
            a = 0
            modules = [name for name in os.listdir(gmmainfile) if os.path.isdir(os.path.join(gmmainfile, name))]
            for i in modules:
                a += 1
                print(a,i)
            allmod = len(modules)
            if allmod == 1:
              print("Only 1 mod detected in the Module Folder!")
              print("The current mod last_module_warband will be written to avoid possible errors!")
              changemodules = open(gmfilemodules,"w")
              changemodules.write(modules[0])
              print("The found mod has been successfully written!")
              process = 0
            choice1 = int(input("""Modules in the Modules folder. Please Select.-->"""))
            if choice1 > allmod:
              os.system("clear")
              print("Invalid Operation!")
            elif choice1 < 1:
              os.system("clear")
              print("Invalid Operation!")
            else:
              changemodules = open(gmfilemodules,"w")
              changemodules.write(modules[choice1-1])
              changemodules.close()
              os.system("clear")
              print("Your game module set to"+modules[choice1-1])
              time.sleep(0.5)
              process = 0
            #Try Except ile int sorununu düzelt !
    elif choice == "2":
      os.system("clear")
      print("Game Directories are controlling!")
      user = os.environ['USER']
      print("Searching for the directory where the game is installed. . .")
      steamdir = "/home/"+user+"/.steam/debian-installation/steamapps/common/MountBlade Warband"
      steamdircontrol = os.path.isdir(steamdir)
      if steamdircontrol == False:
        choice0 = input("Could not detect your game file, please specify the directory where the game is installed!")
        #Oyunu crack indirip dosya sistemini incele!
      else:
        gamefiledir = "/home/"+user+"/.mbwarband"
        gamefilecontrol = os.path.isdir(gamefiledir)
        if gamefilecontrol == False:
          print("The game's files containing config information could not be found. Please specify the directory!")
          #Crack... belkide başka hata kim bilebilir bunla ilgili bilgilendirici yazı yaz!
          gmfilemodules = gamefiledir+"/last_module_warband"
          gmmainfile = steamdir+"/Modules/"
        print("The directory where the game is installed has been detected!")
        process = 3
        os.system("clear")
      while process == 3:
       print("Key files are being scanned!")
       pattern = 'serial_key*'
       keylist =fnmatch.filter(os.listdir(gamefiledir), pattern)
       print("Which Mod would you like to change the key of?")
       a = 1
       for eleman in keylist:
         if eleman in "serial_key":
           print(a,"- Native Key")
         elif eleman in "serial_key_nw":
           print(a,"- Napoleonic Wars Key")
           a +=1
       allkey = len(keylist)
       choice2 = int(input("-->"))
       if choice2 > allkey:
         print("Invalid Operation!")
       elif allkey < 1:
         print("Invalid Operation!")
       else:
         keyloc = gamefiledir+"/"+keylist[choice2-1]
         key = input("Enter Key -->")
         changekey = open(keyloc,"w")
         changekey.write(key)
         changekey.close()
         os.system("clear")
         print("The key was successfully changed. You are transferred to the main menu!")
         process = 0
    else:
      process = 0
      os.system("clear")
      print("Invalid Operation!")
      



