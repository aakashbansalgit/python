import cv2
img = cv2.imread('lena.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',img)
k = cv2.waitKey(0)


if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lenacopy.png',img)
    cv2.destroyAllWindows()
    



