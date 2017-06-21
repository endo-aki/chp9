# coding: UTF-8

from PIL import Image
import numpy as np 
import cv2
import matplotlib.pyplot as plt 


#画像読み込み
img = np.array( Image.open('messi5.jpg') )

#座標
M = np.float32([[1,0,0],[0,1,0]])
dst = cv2.warpAffine(img,M,(1000,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

rows,cols = img.shape[:2]

x,y = (1000,1000)

M = np.float32([[1,0,0],[0,1,1000-rows]])
dst = cv2.warpAffine(dst,M,(1000,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


#テンプレートを保存
tmp = dst

#拡大縮小

res1 = cv2.resize(img,None,fx=0.7,fy=1.5,interpolation=cv2.INTER_CUBIC)
rows,cols = res1.shape[:2]

M = np.float32([[1,0,0],[0,1,1000-rows]])
dst = cv2.warpAffine(res1,M,(1000,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


res2 = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
rows,cols = res2.shape[:2]

M = np.float32([[1,0,0],[0,1,1000-rows]])
dst = cv2.warpAffine(res2,M,(1000,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

rows,cols = img.shape[:2]

#回転

M = np.float32([[1,0,300],[0,1,-200]])
dst = cv2.warpAffine(tmp,M,(1000,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

M = cv2.getRotationMatrix2D((0,1000),45,1)
dst = cv2.warpAffine(dst,M,(1000,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


#鏡映

M = np.float32([[1,0,0],[0,1,0]])
tmp2 = cv2.warpAffine(tmp,M,(1500,1000))
plt.imshow(tmp)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

M = np.float32([[-1,0,1500],[0,1,0]])
dst = cv2.warpAffine(tmp2,M,(1500,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

M = np.float32([[1,0,0],[0,-1,1000]])
dst = cv2.warpAffine(tmp2,M,(1500,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


M = np.float32([[0,-1,1000],[-1,0,1000]])
dst = cv2.warpAffine(tmp2,M,(1500,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

M = np.float32([[0,1,0],[1,0,0]])
dst = cv2.warpAffine(tmp2,M,(1500,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


#スキュー
M = np.float32([[1,-0.5,500],[0,1,0]])
dst = cv2.warpAffine(tmp,M,(1000,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

M = np.float32([[1,0,0],[-1,1,0]])
dst = cv2.warpAffine(tmp,M,(1000,1000))
plt.imshow(dst)
plt.xlabel("x")
plt.ylabel("y")
plt.show()




#アフィン変換
img = cv2.imread('drawing.png')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
plt.xlabel("x")
plt.ylabel("y")

plt.show()


pts1 = np.float32([[0,0],[cols-1,0],[0,rows-1]])
pts2 = np.float32([[0,100],[200,0],[100,300]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
plt.xlabel("x")
plt.ylabel("y")

plt.show()

#射影変換
img = cv2.imread('drawing.png')
rows,cols,ch = img.shape

pts1 = np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])
pts2 = np.float32([[54,67],[254,23],[34,455],[654,45]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(654,rows))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
plt.xlabel("x")
plt.ylabel("y")

plt.show()
