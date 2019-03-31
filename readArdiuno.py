from time import sleep
import serial
import os

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
		message = """GPUS Report - Motion Detected In Vehicle"""
		os.system("lib messagebird.sms.create --recipient 18646097067 --body {}".format(message))
	print(getVal)
