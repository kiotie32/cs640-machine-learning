#!/usr/bin/python3
import numpy as np
from scipy.io import loadmat
import os,sys
import matplotlib.pyplot as plt

data = loadmat('USPS.mat')
#print(data)
x_train = data['train_data'].T   # train patterns
y_train = data['train_lbl'].T     # train_labels
x_test = data['test_data'].T   # test patterns
y_test = data['test_lbl'].T     # test labels
y_train = y_train.T
y_test = y_test.T

#print(x_train.shape,y_train.shape)
#print(x_test.shape,y_test.shape)

# print(x_train[0].flatten().shape)
c = 0

# l_train = x_train.shape[0]
# l_test = x_test.shape[0]
l_train = 1000
l_test = 1000


for i in range(l_test):
    test_row = x_test[i]
    d_c = []
    for j in range(l_train):
        train_row = x_train[j]
        s = 0
        for z in range(len(train_row)):
            s += (train_row[z] - test_row[z])**2
        s = np.sqrt(s)
        d_c.append(( s,int(y_train[j]) ))
    k = 7
   
    d_c = sorted(d_c)
   
#     for r in d_c:
#         print(r)

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
    if C == y_test[i]:
        c += 1
print("classification result based on the given training and testing data : ")
print(100*c/l_test)
     
   

# for t in d_c:
#   print(t)

d1 = np.concatenate((x_train,y_train),axis=1)
d2 = np.concatenate((x_test,y_test),axis=1)
d = np.concatenate((d1,d2),axis=0)
#print(d.shape)

np.random.shuffle(d)

# create equal sized buckets after shuffling of data
b = []
# b.append(d[0:1859,:])
# b.append(d[1859:3718,:])
# b.append(d[3718:5577,:])
# b.append(d[5577:7436,:])
# b.append(d[7436:9298,:])

b.append(d[0:200,:])
b.append(d[1859:1859+200,:])
b.append(d[3718:3718+200,:])
b.append(d[5577:5577+200,:])
b.append(d[7436:7436+200,:])

A = []

for i in range(5):
    test_b = b[i]
    train_b = b[(i+1)%5]
    for j in range(5):
        if i!=j and j!=(i+1)%5:
            np.concatenate((b[j],train_b),axis=0)
           
    l_test = len(test_b)
    l_train = len(train_b)
    c = 0
    for i in range(l_test):
        test_row = test_b[i]
        d_c = []
        for j in range(l_train):
            train_row = train_b[j]
            s = 0
            for z in range(len(train_row)-1):
                s += (train_row[z] - test_row[z])**2
            s = np.sqrt(s)
            d_c.append(( s,int(train_b[j][-1]) ))
        k = 7

        d_c = sorted(d_c)

    #     for r in d_c:
    #         print(r)

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
        if C == test_b[i][-1]:
            c += 1

#     print()
    A.append(100*c/l_test)
print("result using 5-fold cross validation : ")
print(A)
print("Average: ",np.mean(A))
plt.plot(np.arange(5),A)
plt.show()
