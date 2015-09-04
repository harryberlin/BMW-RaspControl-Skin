#Name: BMWRaspControl SkinUpdater
#Version: v0.4
#Owner: Horst12345

cd /tmp
sudo unzip -o master.zip
sudo cp -Rf BMW-RaspControl-Skin-master/skin.confluence-vertical/ /home/osmc/.kodi/addons/
sudo rm master.zip
sudo rm -Rf BMW-RaspControl-Skin-master
