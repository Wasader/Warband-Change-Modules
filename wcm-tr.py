import os
import time
import fnmatch
process = 0

while process == 0:
 print("""
 Hoşgeldiniz,

 888       888       .d8888b.       888b     d888 
 888   o   888      d88P  Y88b      8888b   d8888 
 888  d8b  888      888    888      88888b.d88888 
 888 d888b 888      888             888Y88888P888 
 888d88888b888      888             888 Y888P 888 
 88888P Y88888      888    888      888  Y8P  888 
 8888P   Y8888      Y88b  d88P      888   "   888 
 888P     Y888       "Y8888P"       888       888
 """)

 choice = input("""Yapmak istediğiniz işlemi seçiniz.
 1-Modul Değiştirmek
 2-Key Değiştirmek
 3-Çıkmak için Q basınız

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
        print("Oyunun Kurulu Olduğu Dizin Aranıyor . . .")
        steamdir = "/home/"+user+"/.steam/debian-installation/steamapps/common/MountBlade Warband"
        steamdircontrol = os.path.isdir(steamdir)
        if steamdircontrol == False:
          choice0 = input("Oyun dosyanız tespit edilemidi lütfen oyunun kurulu olduğu dizini belirtiniz!")
          #Oyunu crack indirip dosya sistemini incele!
        else:
          gamefiledir = "/home/"+user+"/.mbwarband"
          gamefilecontrol = os.path.isdir(gamefiledir)
          if gamefilecontrol == False:
            print("Oyunun config bilgileri içeren dosyalarını bulunamadı. Lütfen dizini belirtin!")
            #Crack... belkide başka hata kim bilebilir bunla ilgili bilgilendirici yazı yaz!
          gmfilemodules = gamefiledir+"/last_module_warband"
          gmmainfile = steamdir+"/Modules/"
        print("Oyun kurulu olduğu dizin tespit edildi!")
        process = 2
        while process == 2:
          if steamdircontrol == True:
            print("Mevcut Moduller!")
            a = 0
            modules = [name for name in os.listdir(gmmainfile) if os.path.isdir(os.path.join(gmmainfile, name))]
            for i in modules:
                a += 1
                print(a,i)
            allmod = len(modules)
            if allmod == 1:
              print("Modül Klasöründe sadece 1 adet mod tespit edildi!")
              print(" Olası hataları önlemek için mevcut mod last_module_warband yazılıcak!")
              changemodules = open(gmfilemodules,"w")
              changemodules.write(modules[0])
              print("Bulunan mod başarıyla yazıldı!")
              process = 0
            try:
             choice1 = int(input("""Modules klasöründe bulunan modüller.Lütfen Seçim Yapınız.-->"""))
            except:
              print("Geçersiz İşlem!")
              continue
            if choice1 > allmod:
              os.system("clear")
              print("Geçersiz İşlem!")
            elif choice1 < 1:
              os.system("clear")
              print("Geçersiz İşlem!")
            else:
              changemodules = open(gmfilemodules,"w")
              changemodules.write(modules[choice1-1])
              changemodules.close()
              os.system("clear")
              print("Oyunuz modulu "+modules[choice1-1]+" olarak ayarlandı")
              time.sleep(0.5)
              process = 0
    elif choice == "2":
      os.system("clear")
      print("Oyun Dizinleri kontral edliyor!")
      user = os.environ['USER']
      print("Oyunun Kurulu Olduğu Dizin Aranıyor . . .")
      steamdir = "/home/"+user+"/.steam/debian-installation/steamapps/common/MountBlade Warband"
      steamdircontrol = os.path.isdir(steamdir)
      if steamdircontrol == False:
        choice0 = input("Oyun dosyanız tespit edilemidi lütfen oyunun kurulu olduğu dizini belirtiniz!")
        #Oyunu crack indirip dosya sistemini incele!
      else:
        gamefiledir = "/home/"+user+"/.mbwarband"
        gamefilecontrol = os.path.isdir(gamefiledir)
        if gamefilecontrol == False:
          print("Oyunun config bilgileri içeren dosyalarını bulunamadı. Lütfen dizini belirtin!")
          #Crack... belkide başka hata kim bilebilir bunla ilgili bilgilendirici yazı yaz!
          gmfilemodules = gamefiledir+"/last_module_warband"
          gmmainfile = steamdir+"/Modules/"
        print("Oyun kurulu olduğu dizin tespit edildi!")
        process = 3
        os.system("clear")
      while process == 3:
       print("Key dosyaları taranıyor!")
       pattern = 'serial_key*'
       keylist =fnmatch.filter(os.listdir(gamefiledir), pattern)
       print("Hangi Modun keyini değiştirmek istersiniz ?")
       a = 1
       for eleman in keylist:
         if eleman in "serial_key":
           print(a,"- Native Key")
         elif eleman in "serial_key_nw":
           print(a,"- Napoleonic Wars Key")
           a +=1
       allkey = len(keylist)
       try:
        choice2 = int(input("-->"))
       except:
        print("Geçersiz İşlem!")
        continue
       if choice2 > allkey:
         print("Geçersiz İşlem!")
       elif allkey < 1:
         print("Geçersiz İşlem")
       else:
         keyloc = gamefiledir+"/"+keylist[choice2-1]
         key = input("Keyi Giriniz -->")
         changekey = open(keyloc,"w")
         changekey.write(key)
         changekey.close()
         os.system("clear")
         print("Key başarılıyla değiştirildi. Ana menüye aktarılıyorsunuz!")
         process = 0
    else:
      process = 0
      os.system("clear")
      print("Geçersiz İşlem!")
      



