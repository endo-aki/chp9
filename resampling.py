# coding: UTF-8

import numpy as np 
import cv2
import matplotlib.pyplot as plt 


#画像読み込み
img = cv2.imread("messi5.jpg")

#スケーリング変更
res = cv2.resize(img,None,fx=0.5,fy=0.5)

nearest = cv2.resize(res,None,fx=4,fy=4,interpolation=cv2.INTER_NEAREST)

linear = cv2.resize(res,None,fx=4,fy=4,interpolation=cv2.INTER_LINEAR)

cubic = cv2.resize(res,None,fx=4,fy=4,interpolation=cv2.INTER_CUBIC)

#画像の出力
cv2.imwrite('REnear.png',nearest)
cv2.imwrite('REbili.png',linear)
cv2.imwrite('REbicu.png',cubic)

#画像読み込み
img = cv2.imread("messi5.jpg",0)

#スケーリング変更
res = cv2.resize(img,None,fx=0.5,fy=0.5)

nearest = cv2.resize(res,None,fx=4,fy=4,interpolation=cv2.INTER_NEAREST)

linear = cv2.resize(res,None,fx=4,fy=4,interpolation=cv2.INTER_LINEAR)

cubic = cv2.resize(res,None,fx=4,fy=4,interpolation=cv2.INTER_CUBIC)


print(nearest[100,100])
print(linear[100,100])
print(cubic[100,100])

invM = np.eye(2)/4.

x,y = np.dot(invM,(100,100))

print(res[x,y])

print(res[y:y+2,x:x+2])
print(res[y-1:y+3,x-1:x+3])


X,Y = (109,58)

print(nearest[Y,X])
print(linear[Y,X])
print(cubic[Y,X])

invM = np.eye(2)/4.

x,y = np.dot(invM,(X,Y))

print(res[int(y),int(x)])

print(res[y:y+2,x:x+2])
print(res[y-1:y+3,x-1:x+3])

# 20
# 17
# 17
# 20
# [[20 13]
#  [19 14]]
# [[27 18 13 13]
#  [28 20 13 13]
#  [26 19 14 14]
#  [28 21 16 15]]
# >>> x
# 27.75
# >>> y
# 14.5

# 20
# 21
# 21
# 20
# [[20 13]
#  [19 14]]
# [[27 18 13 13]
#  [28 20 13 13]
#  [26 19 14 14]
#  [28 21 16 15]]
# >>> x
# 27.25
# >>> y
# 14.5
# >>> 

