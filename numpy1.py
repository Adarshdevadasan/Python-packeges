# -*- coding: utf-8 -*-
"""Numpy1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DOYDULsW4VKEXM0r21_3HOcfNKzppV0C
"""

import numpy as np
a=np.array([1,2,3])
print(a)

a=np.array([[1,2,3],[4,5,6]])
print(a)

n=np.array([[1,2,3],[4,5,6]])
print(n.ndim)

p=np.array([1,2,3])
print(p.ndim)

print(n.itemsize)

print(n.dtype)

print(n.size)
print(p.size)
n.nbytes

r=np.array([(1,2,3,4,5,6),(7,8,9,10,11,12,)])
print(r.shape)
print(r)

ar=np.array([(1,2,3,4),(5,6,7,8)])
ar=ar.reshape(4,2)
print(ar)

#slicing
# the first row is in the 0th index and the second row is in the 1st index
ar1=np.array([(1,2,3,4),(5,6,7,8)])
print(ar1)

#to get the element 3,we want to specify that the index number of first row and the index number of the element
print(ar1[0,2])

#get the specfic row
print(ar1[0,:])

#to print 4 and 6,include 0th index and in that row we want only index 3 and print teh 3rd element which is presented in both rows
print(ar1[0:,3])

ar2=np.array([(1,2,3,4),(3,4,5,8),(5,6,7,9)])
print(ar2[0:,3])
#we want to access theonly elements which are in 1st and the 2nd row.when we write 0:2,3,it won't include the second element(index)
print(ar2[0:2,3])

#linspace----creating numeric sequences.
#it will print the 5 sequences b/w 1 and 3
ls=np.linspace(1,2,3)
print(ls)

#it will print the 10 sequences b/w 1 and 5
ls1=np.linspace(1,3,5)
print(ls1)

#find maximum(large element)from the array
m1 = np.array([1,2,3,4])
print(m1.max())

#find minimum
print(m1.min())

#to get the sum of the array
print(m1.sum())

#axis=0,we get the sum of each colomn
ar3=np.array([(1,2,3,4),(5,6,7,8)])
print(ar3)
print(ar3.sum(axis=0))

#axis=1,so we get the sum of each row
print(ar3.sum(axis=1))

#to find the sqrt of the element
ar4=np.array([(1,2,3,4),(3,4,5,6)])
print(np.sqrt(ar1))

ar4=np.array([(1,2,3,4),(3,4,5,6)])
print(np.std(ar1))

#addition
ad=np.array([(1,2,3,4),(3,4,5,6)])
ad1=np.array([(1,2,3,4),(3,4,5,6)])
print(ad+ad1)

#subtraction
ad = np.array([(1,2,3),(4,5,6)])
ad1=np.array([(1,2,3),(4,5,6)])
print(ad-ad1)

#multiplication
ad = np.array([(1,2,3),(4,5,6)])
ad1=np.array([(1,2,3),(4,5,6)])
print(ad*ad1)

#division
ad = np.array([(1,2,3),(4,5,6)])
ad1=np.array([(1,2,3),(4,5,6)])
print(ad/ad1)

#concat
#vertical stacking
print(np.vstack((ad,ad1)))

# horizontal stacking
print(np.hstack((ad,ad1)))

# to make single  column
print(ad.ravel())

# graphical representation of sin
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show

# graphical representation of cos
x=np.arange(0,3*np.pi,0.1)
y=np.cos(x)
plt.plot(x,y)
plt.show

# graphical representation of tan
x=np.arange(0,3*np.pi,0.1)
y=np.tan(x)
plt.plot(x,y)
plt.show

# using natural log
ex=np.array([1,2,3,4])
print(np.log(ex))

# using log10
print(np.log10(ex))

# creating array from list with type float
a=np.array([[1,2,3],[4,5,6]],dtype='float')
print("array created using passed list:\n",a)

#creating array from tuple
b=np.array((1,2,3))
print("\nArray created using passed tuple:\n",b)

# creating a 3x4 array with all zeros
c=np.zeros((3,4))

print("\nan array initialized with all zeros:\n",c)

# create a constant value array of comolex type
d=np.full((3,3),6,dtype='complex')
print("\n array initialized with all 6s."
       "Array type is complex:\n",d)

# create an array with random values
e=np.random.random((2,2))
print("\n A randomarray:\n",e)

# create a sequencwe of integers
# from to 0 to 30 with steps of 5
f=np.arange(0,30,5)
print('\nA sequential array with steps of 5 :\n,f')

# flatten array
arr=np.array([[1,2,3],[4,5,6]])
flar=arr.flatten()
print("\nOrginal array:\n",arr)
print("fattened array:\n",flar)

