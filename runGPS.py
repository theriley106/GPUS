import json
import os
import random
import time
import requests


lng = 74.4057
lat = 40.0583
while True:
	lng += .001
	lat += .001 if random.randint(1,2) == 2 else 0
	url = "https://us-central1-hackathon-180117.cloudfunctions.net/function-1?long={}&lat={}".format(float(lng), float(lat))
	print url
	try:
		res = requests.get(url)
		score = len(res.json()) + random.randint(25, 50) if random.randint(1,2) == 2 else len(res.json()) + random.randint(25, 50)
	except:
		score = random.randint(30, 50)
	if int(score) == 0:
		score = random.randint(25, 75)
	os.system("""echo '{"lat": """ + str(lat) + """, "lng": -""" + str(lng) + """, "score": """ + str(score) + """}' > data.json""")
	time.sleep(.1)
