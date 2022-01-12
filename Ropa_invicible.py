import cv2
import numpy as np

cap = cv2.VideoCapture('Video1.mp4')

bg = None

# Rojo
rojoBajo1 = np.array([0, 150, 40], np.uint8)
rojoAlto1 = np.array([8, 255, 255], np.uint8)
rojoBajo2 = np.array([170, 150, 40], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

# Azul
azulBajo = np.array([90, 100, 110], np.uint8)
azulAlto = np.array([120, 130, 140], np.uint8)

# Naranja
naranjaBajo = np.array([11, 100, 20], np.uint8)
naranjaAlto = np.array([19, 255, 255], np.uint8)

# Amarillo
amarilloBajo = np.array([20, 100, 20], np.uint8)
amarilloAlto = np.array([32, 255, 255], np.uint8)

# Verde
verdeBajo = np.array([36, 100, 20], np.uint8)
verdeAlto = np.array([70, 255, 255], np.uint8)

# Violeta
violetaBajo = np.array([130, 100, 20], np.uint8)
violetaAlto = np.array([145, 255, 255], np.uint8)

# Rosa
rosaBajo = np.array([146, 100, 20], np.uint8)
rosaAlto = np.array([170, 255, 255], np.uint8)
while True:

	ret, frame = cap.read()
	if ret == False: break

	if bg is None:
		bg = frame

	frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	maskRojo1 = cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
	maskRojo2 = cv2.inRange(frameHSV, rojoBajo2, rojoAlto2)
	mask = cv2.add(maskRojo1,maskRojo2)
	mask = cv2.medianBlur(mask, 13)
	kernel = np.ones((5,5),np.uint8)
	mask = cv2.dilate(mask, kernel, iterations=2)
	areaColor = cv2.bitwise_and(bg, bg, mask=mask)
	maskInv = cv2.bitwise_not(mask)
	sinAreaColor = cv2.bitwise_and(frame,frame,mask=maskInv)
	finalFrame = cv2.addWeighted(areaColor,1,sinAreaColor,1,0)
	cv2.imshow('Frame',frame)
	#cv2.imshow('mask', mask)
	#cv2.imshow('areaColor', areaColor)
	#cv2.imshow('maskInv',maskInv)
	#cv2.imshow('sinAreaColor',sinAreaColor)
	cv2.imshow('finalFrame',finalFrame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()