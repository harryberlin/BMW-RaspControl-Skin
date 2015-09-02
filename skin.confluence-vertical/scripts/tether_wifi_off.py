import os
import xbmc,xbmcgui

os.system("sudo connmanctl tether wifi off")
xbmc.executebuiltin("Notification(Tether Wifi,turned off,250)")
pass
