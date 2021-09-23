import numpy as np
import cv2
my_img = np.zeros((1080, 1920, 3), dtype = "uint8")

my_img[:]=(0,0,0)# creating circle

cv2.imshow('Window', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Fondo.jpg', my_img)