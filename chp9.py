# coding: UTF-8

import numpy as np 
import matplotlib.pyplot as plt 

#線形変換

f = np.array([
			[1,2],
			[2,3]	
				])

p = np.array([1,2])

print(np.dot(f,p))

print("\n--------------------------------\n")

#拡大縮小

f = np.array([
			[0.75,0],
			[0,1.5]	
				])

p1 = np.array([0,1])
p2 = np.array([1,1])
p3 = np.array([1,0])
p4 = np.array([0,0])

print(np.dot(f,p1))
print(np.dot(f,p2))
print(np.dot(f,p3))
print(np.dot(f,p4))

print("\n--------------------------------\n")

#回転

theta = np.pi/4

f = np.array([
			[np.cos(theta),-np.sin(theta)],
			[np.sin(theta), np.cos(theta)]	
				])

p = np.array([1,1])

print(np.dot(f,p))

print("\n--------------------------------\n")

#鏡映

f = np.array([
			[1,0],
			[0,-1]	
				])

p = np.array([1,1])

print(np.dot(f,p))


f = np.array([
			[-1,0],
			[0,1]	
				])

p = np.array([1,1])

print(np.dot(f,p))

f = np.array([
			[0,1],
			[1,0]	
				])

p = np.array([1,1])

print(np.dot(f,p))

print("\n--------------------------------\n")

#スキュー

theta = np.pi/4

f = np.array([
			[1,np.tan(theta)],
			[0,1]	
				])

p = np.array([1,1])

print(np.dot(f,p))

f = np.array([
			[1,0],
			[np.tan(theta),1]	
				])

p = np.array([1,1])

print(np.dot(f,p))


print("\n--------------------------------\n")

#拡大縮小

f = np.array([
			[5,0],
			[0,4]	
				])

p1 = np.array([0,1])
p2 = np.array([1,1])
p3 = np.array([1,0])
p4 = np.array([0,0])

print(np.dot(f,p1))
print(np.dot(f,p2))
print(np.dot(f,p3))
print(np.dot(f,p4))

f = np.array([[ 0.2 ,  0.  ],
    		   [ 0.  ,  0.25]])

p1 = np.array([0,100])
p2 = np.array([100,100])
p3 = np.array([100,0])
p4 = np.array([0,0])

print(np.dot(f,p1))
print(np.dot(f,p2))
print(np.dot(f,p3))
print(np.dot(f,p4))

print("\n--------------------------------\n")

x = np.linspace(0,2)

sinc = np.sin(np.pi*x)/(np.pi*x)

plt.plot(x,sinc)

t = np.linspace(0,1)

ht = (t**3) -2*(t**2)+1

plt.plot(t,ht,"b")

t = np.linspace(1,2)

ht = -(t**3)+5*(t**2)-8*t+4

plt.plot(t,ht,"b")


plt.xlabel("t")

plt.ylabel("w")

plt.show()

print("\n--------------------------------\n")


x = np.linspace(0,1)

f = 1.0

y = np.sin(2*np.pi*x)

plt.plot(x,y)

fs = 2*f

delta = 1./fs

sample = np.arange(0.25,1,delta)

ref = np.zeros(1000)

x = np.arange(0,1000)/1000.

y = np.sin(2*np.pi*x)

for i in sample:

	fx = np.sin(2*np.pi*i)*np.sin(np.pi*4*(x-i))/(np.pi*4*(x-i))

	ref = ref + fx 

	plt.plot(x,fx)

plt.show()

plt.plot(x,y)
plt.plot(x,ref, "r")

plt.show()