import os
import xbmc,xbmcgui

os.system("sudo connmanctl tether wifi on")
xbmc.executebuiltin("Notification(Tether Wifi,turned on,250)")
pass