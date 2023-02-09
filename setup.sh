echo "Hello! Starting up!"

# Installing the apps
sudo snap install krita
sudo snap install pycharm-community --classic
sudo apt install wget
sudo apt-get install unzip
sudo apt-get install python3
sudo snap install code -classic
sudo apt update

# Making the dir

# Making the VN and Apps folder
mkdir VNs
mkdir Apps
# Going into the Documents folder
cd Documents
# Making the Code folder
mkdir Code
# Going into the Code folder
cd Code
# Making the Python and HTMl folder
mkdir Python
mkdir HTML
# Going back to home.
cd -
cd -
cd -
cd Apps
mkdir Renpy
mkdir OSU!
cd --
ls
cd VNs
mkdir Werewolf
cd Werewolf
mkdir VN
mkdir Packs
cd --
cd Apps
wget -O renpy https://www.renpy.org/dl/8.0.3/renpy-8.0.3-sdk.tar.bz2
unzip renpy-8.0.3-sdk.tar.bz2
cd - 

# Finishing Set-up
sudo apt update
sudo apt upgrade
python3 finish.py
