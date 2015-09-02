import os
import xbmc
import time

xbmc.executebuiltin('XBMC.Quit')
time.sleep(1)
os.system("sudo reboot -h now")
pass
