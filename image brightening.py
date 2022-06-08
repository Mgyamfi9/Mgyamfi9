import numpy as np
import cv2
##brightening the image
img_unchanged=cv2.imread('bmw.jpg',1)
img1=cv2.resize(img_unchanged,(480,320))
LAB=cv2.cvtColor(img1,cv2.COLOR_BGR2LAB)
L,A,B=cv2.split(LAB)
L_proc=np.where(L<40,cv2.add(L,50),L)
LAB_new=cv2.merge([L_proc,A,B])
result=cv2.cvtColor(LAB_new,cv2.COLOR_LAB2BGR)
cv2.imwrite('brightenedbmw.jpg',result)
cv2.imshow('img1',img1)
##cv2.imshow('L',L)
##cv2.imshow('L_proc',L_proc)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()


###displaying the two images
result=cv2.imread('brightenedbmw.jpg')
img1=cv2.imread('bmw.jpg')
img1=cv2.resize(img1,(480,320))
h1,w1=result.shape[:2]
h2,w2=img1.shape[:2]
img5=np.zeros((h1+h2, max(w1,w2),3),dtype=np.uint8)
img5[:,:]=(255,255,255)
img5[:h1,:w1,:3]=img1
img5[h1:h1+h2, :w2,:3]=result

##cv2.imshow('img3', img3)
##cv2.imshow('img4', img4)
cv2.imshow('img5', img5)
cv2.waitKey(0)
cv2.destroyAllWindows()
