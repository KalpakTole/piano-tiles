import numpy as np
import cv2
from PIL import ImageGrab
from pynput.mouse import Button, Controller
import time
import keyboard


mouse = Controller()
i=0
time_start = time.time()
add = 20
time_check = 40

while(i<100):
	mousePosX = mouse.position[0]
	if 480 < mousePosX < 880:
		img = ImageGrab.grab(bbox = (480, 375, 880, 480))	# (left_x, top_y, right_x, bottom_y) # 	555, 380, 800, 400  # 535, 375, 820, 480
		img_np = np.array(img)
		# frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
		frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
		lower = np.array([0, 0, 0])
		upper = np.array([180, 255, 220])
		mask = cv2.inRange(frame, lower, upper)
		# print(frame)
		output = cv2.bitwise_not(mask)
		# cv2.imshow("Output.jpg", frame)

		# thresh = 240
		# frame_bw = cv2.threshold(frame, thresh, 255, cv2.THRESH_BINARY)[1]
		# print(frame_bw)
		# cv2.imshow("Output_BW.jpg", output)
		

		ypos = np.where(output == 0)[0][i]
		xpos = np.where(output == 0)[1][i]
		# cv2.imshow("Output.jpg", output)

		if output[ypos+5,xpos+5] == 0 and output[ypos+5,xpos] == 0 and output[ypos,xpos+5] == 0: #1st number vertically and 2nd number horizontally
			mouse.position = (xpos+25+480,ypos+add+375)
			# break
			mouse.click(Button.left, 1)
			i=0
			# time.sleep(0.235)
		else:
			i+=1

		
		if keyboard.is_pressed('Esc'):
			break

		if time.time() - time_start > time_check:
			add += 15
			time_check += 20

		'''
		for y in range(len(frame_bw)):
			for x in range(len(frame_bw[y])):
				if frame_bw[y][x]<10:
					mouse.position = (x+480,y+375)
					mouse.click(Button.left,1)
					pass
		'''

# cv2.imshow("Output.jpg", output)
cv2.waitKey(0)
cv2.destroyAllWindows()


# highscore = 712
# This is the site for playing piano tiles:
# http://tanksw.com/piano-tiles/