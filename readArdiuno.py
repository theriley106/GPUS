from time import sleep
import serial
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
	print(getVal)
