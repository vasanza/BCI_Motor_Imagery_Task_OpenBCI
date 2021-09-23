import numpy as np
import cv2
my_img = np.zeros((1080, 1920, 3), dtype = "uint8")
my_img[:]=(250,250,250)

# creating for line
#cv2.line(my_img, (960, 1080), (960, 0), (255, 255, 255), 3)
#cv2.line(my_img, (0, 540), (1920, 540), (255, 255, 255), 3)

cv2.line(my_img, (1720, 980), (1520, 980), (0, 0, 0), 3)#Linea vertical
cv2.line(my_img, (1720,980 ), (1720,780 ), (0, 0, 0), 3) #Linea vertical

cv2.line(my_img, (960, 640), (960, 440), (0, 0, 0), 3)#Linea vertical
cv2.line(my_img, (860, 540), (1060, 540), (0, 0, 0), 3) #Linea Horizontal
cv2.imshow('Window', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('InfDe.jpg', my_img)