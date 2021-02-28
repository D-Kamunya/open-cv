import cv2

Display images
img = cv2.imread("Resources/wiz.jpg")

cv2.imshow("Wiz",img)
cv2.waitKey(0)
