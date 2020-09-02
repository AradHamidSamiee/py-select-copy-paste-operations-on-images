import numpy as np
import cv2
import urllib.request
import matplotlib.pyplot as plt
print("OpenCV-Python Version %s" % cv2.__version__)

req = urllib.request.urlopen('https://cdn.eso.org/images/thumb300y/eso1907a.jpg')
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
# image = cv2.imread('image5.png')

# display an image using matplotlib
# plt.imshow(img) shown an image with wrong colorspace
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# Accessing and Modifying pixel values
px = image[100,100]
print(px)
image[100,100] = [255,255,255]
print(image[100,100])

# Change pixel values
# for i in range(5):
#     for j in range(5):
#         image[50+i, 235+j] = (0, 255, 0)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.show()

# Accessing Image Properties
print(image.shape)
print(image.size)
print(image.dtype)

# Image ROI
part_of_image = image[80:200, 200:320]
# image[0:120, 120:240] = part_of_image
image[100:220 , 0:120] = part_of_image
# this is how it works:
# x: starting point:   0 , destination: 100
# y: starting point: 120 , destination: 220
# output : [100:220 , 0:120]

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
