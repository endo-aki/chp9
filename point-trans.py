# coding: UTF-8

import numpy as np 
import matplotlib.pyplot as plt 

print("\n--------------------------------\n")

p = np.array([1,2])

f = np.array([
			[1,2],
			[2,3]	
				])

fp = np.dot(f,p)

plt.plot(fp[0],fp[1],'bo')

plt.plot(p[0],p[1],'ro')

plt.grid()
plt.xlim([0,10])
plt.xticks( np.arange(0, 10, 1) )
plt.ylim([0,10])
plt.yticks( np.arange(0, 10, 1) )

plt.show()

print("\n--------------------------------\n")

f = np.array([
			[2,0],
			[0,3]	
				])

p = np.array([[1,1],
			  [1,2],
			  [2,2],
			  [2,1]])


plt.plot(p.T[0],p.T[1],'bo')
plt.fill(p.T[0],p.T[1],color="b",alpha=0.5)

fp = np.dot(f,p.T)

plt.plot(fp[0],fp[1],'ro')
plt.fill(fp[0],fp[1],color="r",alpha=0.5)

x = np.vstack((p.T[0],fp[0])).T

y = np.vstack((p.T[1],fp[1])).T

for i in range(4):
	plt.plot(x[i],y[i],'g-')

plt.grid()
plt.xlim([0,10])
plt.xticks( np.arange(0, 10, 1) )
plt.ylim([0,10])
plt.yticks( np.arange(0, 10, 1) )

plt.show()

print("\n--------------------------------\n")

o = np.array([0,0])

t = np.linspace(0,1)

x = np.cos(np.pi*t)

y = np.sin(np.pi*t)

plt.plot(x,y)

theta = np.pi/4

f = np.array([
			[np.cos(theta),-np.sin(theta)],
			[np.sin(theta), np.cos(theta)]	
				])

p = np.array([1,0])

fp = np.dot(f,p)

ffp = np.dot(f,fp)

theta = np.pi/6

g = np.array([
			[np.cos(theta),-np.sin(theta)],
			[np.sin(theta), np.cos(theta)]	
				])

gffp = np.dot(g,ffp)

theta = np.pi/3

h = np.array([
			[np.cos(theta),-np.sin(theta)],
			[np.sin(theta), np.cos(theta)]	
				])

hgffp = np.dot(h,gffp)

pts = np.c_[p,fp,ffp,gffp,hgffp]

linx = np.vstack((np.zeros(5),pts[0])).T

liny = np.vstack((np.zeros(5),pts[1])).T

for i in range(5):
	plt.plot(linx[i,1],liny[i,1],'bo')
	plt.plot(linx[i],liny[i],'r-')

plt.grid()

plt.show()

print("\n--------------------------------\n")

p = np.array([[1,1],
			  [1,2],
			  [2,2],
			  [2,1]])

plt.plot(p.T[0],p.T[1],'bo')
plt.fill(p.T[0],p.T[1],color="b",alpha=0.5)


plt.hlines(y=[0],xmin=-3,xmax=3,colors='g',linewidths=3)
plt.vlines(x=[0],ymin=-3,ymax=3,colors='y',linewidths=3)
x = np.linspace(-3,3)
y = -x
plt.plot(x,y,'r')


f = np.array([
			[1,0],
			[0,-1]	
				])

fp = np.dot(f,p.T)

plt.plot(fp[0],fp[1],'go')
plt.fill(fp[0],fp[1],color="g",alpha=0.5)


f = np.array([
			[-1,0],
			[0,1]	
				])

fp = np.dot(f,p.T)

plt.plot(fp[0],fp[1],'yo')
plt.fill(fp[0],fp[1],color="y",alpha=0.5)


f = np.array([
			[-1,0],
			[0,-1]	
				])

fp = np.dot(f,p.T)

plt.plot(fp[0],fp[1],'ro')
plt.fill(fp[0],fp[1],color="r",alpha=0.5)

plt.grid()
plt.xlim([-3,3])
plt.xticks( np.arange(-3, 3, 1) )
plt.ylim([-3,3])
plt.yticks( np.arange(-3, 3, 1) )

plt.show()

print("\n--------------------------------\n")

#スキュー

p = np.array([[0,0],
			  [0,1],
			  [1,1],
			  [1,0]])

plt.plot(p.T[0],p.T[1],'bo')
plt.fill(p.T[0],p.T[1],color="b",alpha=0.5)

theta = np.pi/4

f = np.array([
			[1,np.tan(theta)],
			[0,1]	
				])

fp = np.dot(f,p.T)

plt.plot(fp[0],fp[1],'ro')
plt.fill(fp[0],fp[1],color="r",alpha=0.5)

plt.grid()
plt.xlim([0,2])
plt.xticks( np.arange(0, 2, 1) )
plt.ylim([0,2])
plt.yticks( np.arange(0, 2, 1) )
plt.show()




p = np.array([[0,0],
			  [0,1],
			  [1,1],
			  [1,0]])

plt.plot(p.T[0],p.T[1],'bo')
plt.fill(p.T[0],p.T[1],color="b",alpha=0.5)

theta = np.pi/4

f = np.array([
			[1,0],
			[np.tan(theta),1]	
				])

fp = np.dot(f,p.T)

plt.plot(fp[0],fp[1],'ro')
plt.fill(fp[0],fp[1],color="r",alpha=0.5)

plt.grid()
plt.xlim([0,2])
plt.xticks( np.arange(0, 2, 1) )
plt.ylim([0,2])
plt.yticks( np.arange(0, 2, 1) )
plt.show()
