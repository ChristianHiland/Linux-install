import os as s
import time as t

print("Checking folders if they have been made.")
t.sleep(5)
print(" ")

# Specifing paths
vn = 'VNs'
apps = 'Apps'
python = 'Documents/Code/Python'
html = 'Documents/Code/HTML'
renpy = "Apps/renpy-8.0.3-sdk.tar.bz2"

# Checking if they exist
vnExist = s.path.exists(vn)
AppsExist = s.path.exists(apps)
PythonExist = s.path.exists(python)
HtmlExist = s.path.exists(html)
RenpyExist = s.path.exists(renpy)

if vnExist == bool(True):
  print("VNs folder has been made")
  if AppsExist == bool(True):
    print("Apps folder has been made")
    if PythonExist == bool(True):
      print("Python folder has been made")
      if HtmlExist == bool(True):
        print("HTML folder has been made")
        print(" ")
        print("Complete: All folders have been made.")
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
print(" ")
print("Checking if files have been installed.")
t.sleep(3)

if RenpyExist == bool(True):
  print("Renpy was installed")
else:
  print("Renpy was not installed, please check the Apps folder. If the file has unziped.")