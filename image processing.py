#image processing
#load libraries

import numpy as np
import cv2

#load and color an image in grayscale and resize the image, increase image brightness
img_unchanged=cv2.imread('minions.jpg',1)
img_gray=cv2.imread('minions.jpg',0)
img1=cv2.resize(img_gray,(320,240))
img2=cv2.resize(img_unchanged,(320,240))

#saving the image
cv2.imwrite('grayminions.png', img1)

#displaying the image
cv2.imshow('grayminions',img1)
cv2.imshow('minions', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#displaying the two images
img3=cv2.imread('grayminions.png')
img_4=cv2.imread('minions.jpg')
img4=cv2.resize(img_4,(320,240))
h1,w1=img3.shape[:2]
h2,w2=img4.shape[:2]
img5=np.zeros((h1+h2, max(w1,w2),3),dtype=np.uint8)
img5[:,:]=(255,255,255)
img5[:h1,:w1,:3]=img3
img5[h1:h1+h2, :w2,:3]=img4

##cv2.imshow('img3', img3)
##cv2.imshow('img4', img4)
cv2.imshow('img5', img5)
cv2.waitKey(0)
cv2.destroyAllWindows()



