# coding: UTF-8

import numpy as np 
import cv2
import matplotlib.pyplot as plt 


#画像読み込み
img = cv2.imread("messi5.jpg")

print(img.shape)

#スケーリング変更
res1 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

res2 = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)

res3 = cv2.resize(img,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_CUBIC)

#画像の出力
cv2.imwrite('2x2scaling.png',res1)
cv2.imwrite('05x05scaling.png',res2)
cv2.imwrite('03x03scaling.png',res3)