import cv2

img = cv2.imread('lena.jpg',1)
img = cv2.line(img, (0,0), (480,640),(2,255,2), 5)
img = cv2.arrowedLine(img, (0,0), (255,255),(255,3,54), 5)
img = cv2.rectangle(img, (380,0), (510,128), (0,0,255), 5)
img = cv2.circle(img, (447,63), 63, (100,100,100), -1)
font = cv2.FONT_HERSHEY_COMPLEX()
img = cv2.putText(img, "OpenCV", (10, 500), font, 4, (32,32,32), 10, v2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()