#!/usr/bin/python3
import numpy as np
from scipy.io import loadmat
import os,sys
import matplotlib.pyplot as plt

mnist = loadmat('MNIST.mat')
# print(mnist)
x_train = mnist['train_data'].T
y_train = mnist['train_lbl']
x_test = mnist['test_data'].T
y_test = mnist['test_lbl']
#print(x_train.shape,y_train.shape)
#print(x_test.shape,y_test.shape)

# d1 = np.hstack(x_train,y_train)
# d2 = no.hstack(x_test,y_test)

# print(y_test[0])

# print(x_train[0].flatten().shape)
c = 0

l_train = 6000
l_test = 50


for i in range(l_test):
  test_row = x_test[i].flatten()
  d_c = []
  for j in range(l_train):
    train_row = x_train[j].flatten()
    s = 0
    for x in range(len(train_row)):
      s += (train_row[x] - test_row[x])**2
    s = np.sqrt(s)
    d_c.append([s,int(y_train[j])])
  k = 7
#   for r in d_c:
#     print(r)
  d_c = sorted(d_c)
 
  freq = {}
  M = 0
  C = 0
  for j in range(k):
    if d_c[j][1] not in freq:
      freq[ d_c[j][1] ] = 1
    else:
      freq[ d_c[j][1] ] += 1
    if freq[ d_c[j][1] ] > M:
      M = freq[ d_c[j][1] ]
      C = d_c[j][1]
#   print(freq)
  if C == int(y_test[i]):
    c += 1

print(100*c/l_test)
     
   

# for t in d_c:
#   print(t)

import matplotlib.pyplot as plt

A_mnist = [84,80,100,96,96]
A_usps = [86,84.5,76.5,84,78]
plt.plot(np.arange(5),A_mnist,label='MNIST')
plt.plot(np.arange(5),A_usps,label='USPS')
plt.legend(loc='upper left')
plt.show()
