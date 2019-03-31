from time import sleep
import serial
import os
import requests




ser = serial.Serial("/dev/ttyACM1",9600)
count = 0
while True:
	sleep(.1)
	getVal = ser.readline()
	if int(getVal) == 0:
		count = 0
	else:
		count += 1
	if count > 8:
		print("CRASH DETECTED")
		res = requests.get("/currentPosition")
		x = res.json()
		message = """GPUS Report - Accident Detected in Nathan's Vehicle at {} {}.  Emergency vehicles have been dispatched""".format(x['lat'], x['lng'])
		os.system("lib messagebird.sms.create --recipient 18645674106 --body {}".format(message))
	print(getVal)
