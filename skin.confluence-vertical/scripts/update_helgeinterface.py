#Name: BMWRaspControl HelgeIntefaceUpdater
#Version: v0.4
#Owner: Horst12345
#2015/09/03 changed for HelegInerface by The Mischen

import urllib,os,re,urllib2
import xbmc,xbmcgui

skindir = xbmc.getSkinDir()
 
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("BMWRaspControl Update","Lade Datei", "BMW RaspControl HelgeInterface - Update")
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))

def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "Download Abgebrochen"
        dp.close()		
	quit()
	
def checkinternet():
    try:
        response=urllib2.urlopen('http://173.194.32.223',timeout=2)
        return True
    except urllib2.URLError as err: pass
    return False

dialog = xbmcgui.Dialog()
if dialog.yesno("BMW RaspControl HelgeInterfaceupdater", "Are you sure to update The HelgeInterface?") == 1:
    if checkinternet() == 1:
            url ='http://bmwraspcontrol.de/software/HelgeInterface_last.zip'
            DownloaderClass(url,"/tmp/HelgeInterface.zip")
            os.system('sh /home/osmc/.kodi/addons/skin.confluence-vertical/scripts/update_helgeinterface.sh')
            xbmc.executebuiltin("ReloadSkin()")
            xbmc.executebuiltin("Notification(BMWRaspControl HelgeInterface Updater,Update erfolgreich!,500)")
    else:
            xbmc.executebuiltin("Notification(BMWRaspControl HelgeInterface Updater,VERBINDUNGSFEHLER!,500)")
pass