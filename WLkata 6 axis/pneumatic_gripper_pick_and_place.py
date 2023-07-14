#version python 3.8
#coding=utf-8
from mirobot import *
from time import sleep
api=Mirobot()
#Please do not delete the above code
api.home_simultaneous()

H1, H2, H3, H4, H5, H6 = 0, 0, 0, 0, 0, 0
A1, A2, A3, A4, A5, A6 = -50, 32, 25, 0, -55, 0
AP1, AP2, AP3, AP4, AP5, AP6 =  -50, 30, 25, 0, -55, 0

B1, B2, B3, B4, B5, B6 = 50, 32, 25, 0, -55, 0
BP1, BP2, BP3, BP4, BP5, BP6 = 50, 30, 25, 0, -55, 0

for i in range(5):
## pick and place A to B
	#home
	api.go_to_axis(H1, H2, H3, H4, H5, H6)
	#end point mid & A
	api.go_to_axis(AP1, AP2, AP3, AP4, AP5, AP6)
	sleep(1)
	api.go_to_axis(A1, A2, A3, A4, A5, A6)
	api.suction_cup_on() # open
	sleep(2)

	#home
	api.go_to_axis(H1, H2, H3, H4, H5, H6)
	#end point mid & B
	api.go_to_axis(BP1, BP2, BP3, BP4, BP5, BP6)
	sleep(1)
	api.go_to_axis(B1, B2, B3, B4, B5, B6)
	api.suction_cup_off() # close
	sleep(2)
	api.go_to_axis(BP1, BP2, BP3, BP4, BP5, BP6)
	sleep(1)

## pick and place B to A
	#home
	api.go_to_axis(H1, H2, H3, H4, H5, H6)
	#end point mid & B
	api.go_to_axis(BP1, BP2, BP3, BP4, BP5, BP6)
	sleep(1)
	api.go_to_axis(B1, B2, B3, B4, B5, B6)
	api.suction_cup_on() # open
	sleep(2)

	#home
	api.go_to_axis(H1, H2, H3, H4, H5, H6)
	#end point mid & A
	api.go_to_axis(AP1, AP2, AP3, AP4, AP5, AP6)
	sleep(1)
	api.go_to_axis(A1, A2, A3, A4, A5, A6)
	api.suction_cup_off() # close
	sleep(2)
	api.go_to_axis(AP1, AP2, AP3, AP4, AP5, AP6)
	sleep(1)

	#reset
	api.go_to_axis(H1, H2, H3, H4, H5, H6)
	

