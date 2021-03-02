import cv2
import numpy as np
# Display images
img = cv2.imread("Resources/wiz.jpg")

# cv2.imshow("Wiz",img)
# cv2.waitKey(0)

# Display videos
# cap=cv2.VideoCapture("Resources/test.mp4")

# while True:
#   success, img = cap.read()
#   cv2.imshow("video",img)
#   if cv2.waitKey(1) & 0xFF ==ord('q'):
#     break

# Using webcam
# cap=cv2.VideoCapture(0)
# cap.set(3,640) # Set width id no is 3
# cap.set(4,480) # set height id no is 4
# cap.set(10,100) # Define the brightness

# while True:
#   success, img = cap.read()
#   cv2.imshow("video",img)
#   if cv2.waitKey(1) & 0xFF ==ord('q'):
#     break

# img = cv2.imread("Resources/wiz.jpg")
# kernel=np.ones((5,5),np.uint8)
# # Convert image to grayscale (2 params;img to be converted and color space)
# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # Blur image using cv
# imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
# # Edge detector using Canny(100 are the threshhols values)
# # To reduce edges increase threshhold
# imgCanny=cv2.Canny(img,150,200)
# # Dialate image filters ie increase thickness of edges just incase of breakages in images
# # Increase iterations for more thickness
# imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
# # Make edges thinner ie erode
# imgEroded=cv2.erode(imgDialation,kernel,iterations=1)

# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Dialation Image",imgDialation)
# cv2.imshow("Eroded Image",imgEroded)
# cv2.waitKey(0)
# 0xFF ==ord('q')


# Resizing Images
#Find the size
print(img.shape) #returns tuple with H,W and channels(BGR)
imgResize=cv2.resize(img,(400,400))
print(imgResize.shape)
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.waitKey(0)
0xFF ==ord('q')