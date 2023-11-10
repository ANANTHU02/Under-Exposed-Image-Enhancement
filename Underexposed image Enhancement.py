import cv2
import matplotlib.pyplot as plt
from numpy import asarray
from skimage import img_as_ubyte
import numpy as np
import math
img=cv2.imread(r'D:\Documents\MSc MI\Sem 2\Mini project\image5\image5.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=img_as_ubyte(img)
#gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
plt.imshow(img)
plt.show()
#blurring image
#img=cv2.GaussianBlur(img, (3, 3), 0)
#converting image to array
img_array=asarray(img)
row=img_array.shape[0]
col=img_array.shape[1]
channel=img_array.shape[2]
a=43.0
intensity_min=0.0
intensity_max=254.0

#1.linear transformation

for i in range(row):
    for j in range(col):
        for k in range(channel):
            if(img_array[i][j][k]>=0 and img_array[i][j][k]<=a):
                img_array[i][j][k]=np.uint8(np.clip(3.0*img_array[i][j][k],intensity_min,intensity_max))
            elif(img_array[i][j][k]>a and img_array[i][j][k]<=2*a):
                img_array[i][j][k]=np.uint8(np.clip(img_array[i][j][k]-a+a*3.0,intensity_min,intensity_max))
            else:
                img_array[i][j][k]=np.uint8(np.clip(2.0/3.0*(img_array[i][j][k]-a*2)+a*4,intensity_min,intensity_max))

img_array=cv2.cvtColor(img_array,cv2.COLOR_BGR2RGB)
img=img_as_ubyte(img_array)
plt.imshow(img)
plt.show()
cv2.imwrite('D:\Documents\MSc MI\Sem 2\Mini project\Image dataset\image_1_enhanced.jpg',img)

#2.log transformation
"""for i in range(row):
    for j in range(col):
        for k in range(channel):
            img_array[i][j][k]=np.uint8(np.clip(math.log1p(50.0*img_array[i][j][k]),intensity_min,intensity_max))
plt.imshow(img_array)
plt.show()  
cv2.imwrite('D:\Documents\MSc MI\Sem 2\Mini project\chumma_log.jpg',img)
#power function
img=np.uint8(np.clip(pow(img,3.0),intensity_min,intensity_max))
plt.imshow(img)
plt.show()    
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imwrite('D:\Documents\MSc MI\Sem 2\Mini project\image10\image10_power3.jpg',img)

#3.CLAHE method

img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
h,s,v=img[:,:,0],img[:,:,1],img[:,:,2]
clahe=cv2.createCLAHE(clipLimit=5.0,tileGridSize=(1,1))
v=clahe.apply(v)
img=np.dstack((h,s,v))
img=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
plt.imshow(img)
plt.show()
cv2.imwrite('D:\Documents\MSc MI\Sem 2\Mini project\image10\image10_clahe.jpg',img)

#4.histogram equalization

img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
h,s,v=cv2.split(img)
v=cv2.equalizeHist(v)
img=cv2.merge((h,s,v))
img=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
img=img_as_ubyte(img)
cv2.imwrite('D:\Documents\MSc MI\Sem 2\Mini project\image10\image10_HE.jpg',img)"""
