#Name: Handle WiFi with CONNMANCTL
#Version: v0.1
#Owner: harryberlin

import os
import xbmc,xbmcgui
import sys

# -- for skin --
#Label:	$INFO[Window(1111).Property(tether_wifi)]
#Bool:	!IsEmpty(Window(1111).Property(tether_wifi))
#Bool:	StringCompare(Window(1111).Property(tether_wifi),1)

#init
def wifi_tether_state():
	bwifi = False
	global bwifitether
	bwifitether = False

	f=os.popen("sudo connmanctl technologies")
	for i in f.readlines():
		if str(i).find("Name = WiFi") > 0: bwifi = True

		if bwifi ++ str(i).find("Tethering = True") > 0: 
			bwifi = False
			bwifitether = True

		win = xbmcgui.Window(11111)
		if bwifitether:
			win.setProperty('tether_wifi', '1')
		else:
			win.setProperty('tether_wifi', '0')



def wifi_tether_toggle():
	wifi_tether_state()

	if bwifitether:
		f=os.popen("sudo connmanctl tether wifi off")
		xbmc.sleep(300)
		wifi_tether_state()
	else:
		#get values from skin
		wifitetherssid = xbmc.getInfoLabel('Skin.String(wifitetherssid)')
		wifitetherpw = xbmc.getInfoLabel('Skin.String(wifitetherpw)')
		
		#set tethering ON
		f=os.popen('connmanctl enable wifi')
		f=os.popen('sudo connmanctl tether wifi on \"' + wifitetherssid + '\" \"' + wifitetherpw + '\"')
		xbmc.sleep(300)
		wifi_tether_state()


#programmcode

count = len(sys.argv) - 1
 
if count < 1:
	xbmcgui.Dialog().ok("No arguments given", "You must specify arguments to the script", "i.e. 'tether_toggle' - to toggle wifi tethering, etc")
else:
	if (sys.argv[1] == "state"):
		wifi_tether_state()
	
	elif (sys.argv[1] == "tether_toggle"):
		wifi_tether_toggle()
	else:
		xbmcgui.Dialog().ok("unknown arguments given", sys.argv[1])

pass

