import os
import xbmc
import time

os.system("sudo service HelgeInterface stop")
time.sleep(1)
xbmc.executebuiltin('XBMC.Powerdown')
pass
