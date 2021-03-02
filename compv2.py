import cv2
import numpy as np

#Binary image
img=np.zeros((512,512))
#Add channels
img=np.zeros((512,512,3),np.uint8)
#Add color
# img[200:400,200:400]=255,0,0

# Add line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)#3 is for thickness (W,H)
cv2.imshow("Image",img)

cv2.waitKey(0)
0xFF==ord('q')