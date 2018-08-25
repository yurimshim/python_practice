# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 13:21:08 2018

@author: LG
"""
import os
os.chdir("C:/Users/LG/Desktop/2018-S/fython")
from csv import reader
import numpy as np
from sklearn.metrics import accuracy_score

# Load a CSV file
def load_csv(filename):
    x_train = list()
    y_train = list()
    file = open(filename, 'r')
    csv_reader = reader(file)
    for row in csv_reader:
        if not row:
            continue
        x_train.append(row)
        y_train.append(row)
    x_train = data_to_float(x_train)
    y_train = data_to_int(y_train)
    file.close()
    return x_train, y_train
        
def data_to_int(trainSet):
    for row in trainSet:
        for column in row:
            column = int(column)
    return trainSet        
    # (여기에 코드 작성)
    # 읽어 온 자료를 numpy 배열로 바꾸고 이 때 x_train과 y_train은 각각 float형과 int형으로 한다.
    # 참고: 강의 자료 중 
# How to Implement Simple Linear Regression From Scratch with Python 참조
def data_to_float(trainSet):
    for row in trainSet:
        for column in row:
            column = float(column)
    return trainSet
 
def one_hot_encoding(ytrain):
    for row in y_train:
        for column in row:
            if column > 0:
                column = 1
            else:
                column = 0
    return y_train
      #y_train 정답 값을 one-hot encoding으로 변형. sklearn, pandas, keras 등에서 제공하는 모듈을 쓰지말고 numpy로 구현해 볼 것  


def init_network(input_size, hidden_size, output_size):
    network = {}
    weight_int_std = 0.01
    network['W1'] = weight_int_std * np.random.randn(input_size, hidden_size)
    network['b1'] = np.zeros(hidden_size)
    network['W2'] = weight_int_std * np.random.randn(hidden_size, hidden_size)
    network['b2'] = np.zeros(hidden_size)
    network['W3'] = weight_int_std * np.random.randn(hidden_size, output_size)
    network['b3'] = np.zeros(output_size)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    y_bf_sigmoid = np.dot(np.array([W1, W2, W3]), np.array([x,x,x])) + np.array([b1,b2,b3])
    y_bf_softmax = sigmoid(y_bf_sigmoid)
    y = softmax(y_bf_softmax)
    # Weight와 bias를 내적한 후 sigmoid로 활성화, 마지막에는 softmax로 확률을 구함
    return y

def accuracy(x, t):      # x는 자료에서 예측된 값 t는 정답으로 주어진 값
    y = predict(network,x)
    accuracy = accuracy_score(y,t)
    
     # 예측된 값과 one_hot_encoding으로 된 y_train값을 비교하여 정확도를 출력
    return accuracy


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x) # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))


filename = 'SimpleNetData.csv'
x_train, y_train = load_csv(filename)
y_train = one_hot_encoding(y_train)

network = init_network(len(x_train[1]), 100, 10)

accuracy = accuracy(x_train, y_train)

print (accuracy)
