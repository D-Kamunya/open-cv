import cv2

# Display images
# img = cv2.imread("Resources/wiz.jpg")

# cv2.imshow("Wiz",img)
# cv2.waitKey(0)

# Display videos
cap=cv2.VideoCapture("Resources/test.mp4")

while True:
  success, img = cap.read()
  cv2.imshow("video",img)
  if cv2.waitKey(1) & 0xFF ==ord('q'):
    break


