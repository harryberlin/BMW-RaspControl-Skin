#Name: BMWRaspControl SkinUpdater
#Version: v0.4
#Owner: Horst12345
#2015/09/03 changed for HelegInerface by The Mischen

cd /tmp
sudo service HelgeInterface stop
sudo service OpenBM stop
sudo mkdir /home/osmc/backup
sudo cp -r /home/HelgeInterface/ /home/osmc/backup/
sudo unzip -o HelgeInterface.zip -x Config/helgeinterface.xml -d /home/HelgeInterface
sudo rm HelgeInterface.zip
sudo service OpenBM start
sudo service HelgeInterface start
# sudo reboot -n