import cv2
import numpy as np
src = "image.png"
mask = "output.png"
# 使用opencv叠加图片
img1 = cv2.imread(src)
img2 = cv2.imread(mask)

alpha = 0.5
meta = 0.5
gamma = 0
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
image = cv2.addWeighted(img1, alpha, img2, meta, gamma)

cv2.imshow('image', image)
cv2.waitKey(0)
