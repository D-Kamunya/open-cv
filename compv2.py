import cv2
import numpy as np

#Binary image
img=np.zeros((512,512))
#Add channels
img=np.zeros((512,512,3),np.uint8)
#Add color
# img[200:400,200:400]=255,0,0

# Add line (define start point and endpoint and color)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)#3 is for thickness (W,H)
# Draw rectangle(define start point and endpoint and color)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
#Fill rectangle
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
# Draw circle(define center point,radius,color,thickness)
cv2.circle(img,(400,50),30,(255,255,0),5)

cv2.imshow("Image",img)

cv2.waitKey(0)
0xFF==ord('q')