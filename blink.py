import RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)
io.setup(18,io.OUT)

i = 0
c = -1
while True:
	if(i == 10) or (i == 0):
		c = 0 - c
	i = i + c
	io.output(18,True)
	sleep(i/10)
	io.output(18,False)
	sleep(i/10)
