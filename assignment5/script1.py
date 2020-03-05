#!/usr/bin/python3
import os
from mat4py import loadmat
os.getcwd()
mat=loadmat('/home/debian/cs640 machine learning/assignment5\MNIST.mat')
print (mat)
