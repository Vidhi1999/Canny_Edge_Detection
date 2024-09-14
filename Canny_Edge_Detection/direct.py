import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\Vidhi\Documents\Canny_Edge_Detection\images\owl.JPG',0)
edges = cv2.Canny(img,100,200)

#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),
plt.imshow(edges,cmap = 'gray')
plt.title(''), plt.xticks([]), plt.yticks([])

plt.show()