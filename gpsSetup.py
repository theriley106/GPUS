from gps import *

import time
import threading
import requests

gpsd = None
class GpsPoller(threading.Thread):
	 def __init__(self):
			 threading.Thread.__init__(self)
			 global gpsd
			 gpsd=gps(mode=WATCH_ENABLE)
			 self.current_value = None
			 self.running = True
	 def run(self):
			 global gpsd
			 while gpsp.running:
					 gpsd.next()
if  __name__ == "__main__":
	 gpsp=GpsPoller()

	 try:
			 gpsp.start()
			 while True:
					 #x =  + "," +  + "\n"
					 #print(x)
					 #f.write(x)
					 url = "https://us-central1-hackathon-180117.cloudfunctions.net/function-1?long={}&lat={}".format(int(float(gpsd.fix.longitude)), int(float(gpsd.fix.latitude)))
					 print url
					 res = requests.get(url)
					 print res.text
					 time.sleep(1)

	 except:
			 #f.close()
			 gpsp.running = False
			 gpsp.join()
