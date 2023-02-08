import os as s
import time as t
import shutil

print("Checking folders if they have been made.\n")
t.sleep(1)

# Specifing paths
vn = 'VNs'
apps = 'Apps'
python = 'Documents/Code/Python'
html = 'Documents/Code/HTML'
renpy = "Apps/Renpy"
renpyshort = "Shortcuts/renpy.desktop"
home = "Desktop"
werewolfVN = "VNs/Werewolf/Werewolf"
packWere = "VNs/Werewolf/Packs"

# Checking if they exist
vnExist = s.path.exists(vn)
AppsExist = s.path.exists(apps)
PythonExist = s.path.exists(python)
HtmlExist = s.path.exists(html)
RenpyExist = s.path.exists(renpy)
WereExist = s.path.exists(werewolfVN)
PacksExist = s.path.exists(packWere)

if vnExist == bool(True):
  print("VNs folder has been made")
  if AppsExist == bool(True):
    print("Apps folder has been made")
    if PythonExist == bool(True):
      print("Python folder has been made")
      if HtmlExist == bool(True):
        print("HTML folder has been made")
        if WereExist == bool(True):
          print("Werewolf folder has been made")
          if PacksExist == bool(True):
            print("Packs folder has been made\n")
            print("Complete: All folders have been made.\n")
          else:
            print("Packs in VNs was not made, check if it was made in the right place.")
        else:
          print("Werewolf in VNs was not made, check if it was made in the right place.")
      else:
        print("HTML was not made, check if it was made in the right place.")
    else:
      print("Python was not made, check if it was made in the right place.")
  else:
    print("Apps was not made, check if it was made in the right place.")
else:
  print("VNs was not made, check if it was made in the right place.")

# Making the files.

# Checking if files are made.

print("Checking if files have been installed.\n")
t.sleep(1)
dir_list = s.listdir(packWere)
if RenpyExist == bool(True):
  print("Renpy was installed")
  print("// Making a shortcut")  
  shutil.move(renpyshort, home)
else:
  print("Renpy was not installed, please check the Apps folder. If the file has unziped.")
