from gps import *

import time
import threading
import requests
import json
import os

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
			 		 try:
						 #x =  + "," +  + "\n"
						 #print(x)
						 #f.write(x)
						 lng = gpsd.fix.longitude
						 lat = gpsd.fix.latitude
						 url = "https://us-central1-hackathon-180117.cloudfunctions.net/function-1?long={}&lat={}".format(float(lng), float(lat))
						 print url
						 res = requests.get(url)
						 data = {"lat": float(lat), 'lng': float(lng), 'score': len(res.json())}
						 with open('data.json', 'w') as outfile:
							json.dump(data, outfile)
						 time.sleep(.1)
					 except Exception as exp:
					 	 a = json.load(open("data.json"))
					 	 a['score'] = 100
						 with open('data.json', 'w') as outfile:
							json.dump(a, outfile)
						 time.sleep(5)

	 except:
			 #f.close()
			 gpsp.running = False
			 gpsp.join()

