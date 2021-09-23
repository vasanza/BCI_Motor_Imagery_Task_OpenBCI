import numpy as np
import cv2
my_img = np.zeros((1080, 1920, 3), dtype = "uint8")
#my_img[:]=(255,255,255)# creating circle
my_img[:]=(0,0,0)# creating circle

#cv2.circle(my_img, (1440, 270), 20, (0, 0, 0), -1)
#cv2.line(my_img, (960, 640), (960, 440), (0, 0, 0), 3)#Linea vertical
#cv2.line(my_img, (860, 540), (1060, 540), (0, 0, 0), 3) #Linea Horizontal

cv2.circle(my_img, (1440, 270), 20, (255, 255, 255), -1)
cv2.line(my_img, (960, 640), (960, 440), (255, 255, 255), 3)#Linea vertical
cv2.line(my_img, (860, 540), (1060, 540), (255, 255, 255), 3) #Linea Horizontal

cv2.imshow('Window', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('RCH.jpg', my_img)