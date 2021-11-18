import numpy as np
import cv2

img=cv2.imread('messi5.jpg')
img2=cv2.imread('opencv-logo.png')

print(img.shape)#returns a tupple of no of rows column and channels
print(img.size)#return a total no of acessed pixel
print(img.dtype)#return imagedata type is obtained
b, g, r =cv2.split(img)
img=cv2.merge((b,g,r))

ball=img[280:340, 330:390]
img[273:333, 100:160] =ball

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

#dst=cv2.add(img,img2); #used to add two images

dst=cv2.addWeighted(img,0.2,img2,0.8,0); #used for more dominant image


cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()