import os
import xbmc,xbmcgui

bTetherWifi = xbmc.getCondVisibility('Skin.HasSetting(tether_wifi)')

if bTetherWifi == 1:
	os.system("sudo connmanctl tether wifi off")
	xbmc.executebuiltin("Skin.Reset(tether_wifi)")
	#xbmc.executebuiltin("Notification(Tether Wifi turned off,,250)")

else:
	os.system("sudo connmanctl tether wifi on")
	xbmc.executebuiltin("Skin.SetBool(tether_wifi)")
	#xbmc.executebuiltin("Notification(Tether Wifi turned on,,250)")

pass