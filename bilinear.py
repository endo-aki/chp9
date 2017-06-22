# coding: UTF-8

from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt 



def scaling1(src,fx,fy):

	img = np.array(src)

	cols,rows,colors = img.shape

	dst = np.zeros((int(fy*cols),int(fx*rows),colors))

	dst = dst.astype('uint8')

	for j in range(cols):
		for i in range(rows):
			if (fy*j - int(fy*j))==0 and (fx*i - int(fx*i))==0:
				dst[int(fy*j),int(fx*i)] = img[j,i]

	destination = Image.fromarray(dst)

	destination.save('scaling1.jpg')

def scaling2(src,fx,fy):

	img = np.array(src)

	cols,rows,colors = img.shape

	dst = np.zeros((int(fy*cols),int(fx*rows),colors))

	dst = dst.astype('uint8')

	dst_cols,dst_rows = dst.shape[:2]

	f = np.array([[fx,0],
				  [0,fy]])

	invf = np.linalg.inv(f)

	for j in range(dst_cols):
		for i in range(dst_rows):
			x,y = np.dot(invf,np.array([i,j]))
			dst[j,i] = img[int(y),int(x)]

	destination = Image.fromarray(dst)

	destination.save('scaling2.jpg')



def scaling3(src,fx,fy):

	img = np.array(src)

	cols,rows,colors = img.shape

	dst = np.zeros((int(fy*cols),int(fx*rows),colors))

	dst = dst.astype('uint8')

	dst_cols,dst_rows = dst.shape[:2]

	f = np.array([[fx,0],
				  [0,fy]])

	invf = np.linalg.inv(f)

	for j in range(dst_cols):
		for i in range(dst_rows):
			x,y = np.dot(invf,np.array([i,j]))

			X = int(x)
			Y = int(y)

			if ((x == X) and (y == Y)) or (((X == rows-1)and(x>X))and((Y == cols-1)and(y>Y))):
				dst[j,i] = img[Y,X]
			elif ((X == rows-1)and(x>X)) or (x == X):
				if Y == cols-1:
					dst[j,i] = img[Y,X]
				else:
					wy = np.array([Y+1-y,y-Y])
					pts = np.array([img[Y,X],img[Y+1,X]])
					dst[j,i] = np.dot(wy,pts)
			elif ((Y == cols-1)and(y>Y)) or (y == Y):
				if X == rows-1:
					dst[j,i] = img[Y,X]
				else:
					wx = np.array([X+1-x,x-X])
					pts = np.array([img[Y,X],img[Y,X+1]])
					dst[j,i] = np.dot(wx,pts)
			else:
				wx = np.array([X+1-x,x-X])
				wy = np.array([Y+1-y,y-Y])

				pts = np.array([[  img[Y,X],  img[Y,X+1]],
								[img[Y+1,X],img[Y+1,X+1]]])

				dst[j,i] = np.dot(wy,np.einsum('ijk,j->ik',pts,wx))
			

	destination = Image.fromarray(dst)

	destination.save('scaling3.jpg')

