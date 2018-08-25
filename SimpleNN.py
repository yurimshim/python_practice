import sys, os
from csv import reader
import numpy as np

# Load a CSV file
def load_csv(filename):
    """load a CSV file
    
    Arguments:
        filename {str} -- absolute path to csv file 
    
    Returns:
        A tuple of np.array : (x_train, y_train)
            x_train: np.array float (5000, 12)
            y_train: np.array int (5000, )
    """

    x_train = list()
    y_train = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)

    # 5000*13의 파일을 (5000, 12) 와 (5000, )으로 나누기!
    # numpy array이니까 제대로 나뉘었는지 확인차 맨 마지막 return 전에
    # assert (x_train.shape == (5000, 12))
    # assert (y_train.shape == (5000, )) 하면 되겠죠?
    
    # (여기에 코드 작성)
    # 읽어 온 자료를 numpy 배열로 바꾸고 이 때 x_train과 y_train은 각각 float형과 int형으로 한다.
    # 참고: 강의 자료 중 
    # How to Implement Simple Linear Regression From Scratch with Python 참조
    

    return x_train, y_train

def one_hot_encoding(y):
    """change y_train to one_hot_encoding
    
    Arguments:
        y {int} -- class from 0~9

        return 을 그럼 어떻게 해야할까요~
    """

    # y_train 정답 값을 one-hot encoding으로 변형. sklearn, pandas, keras 등에서 제공하는 모듈을 쓰지말고 numpy로 구현해 볼 것  

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

    # X * W1 을 하면
    # (5000, 12) * (input_size, hidden_size) => (5000, hidden_size)
    # W3까지 곱하면 결국 y = (5000, output_size) 겠징?
    # 그럼 sigmoid에 넣으면 (5000, output_size) !

    # Weight와 bias를 내적한 후 sigmoid로 활성화, 마지막에는 softmax로 확률을 구함

    return y

def accuracy(x, t):      #x는 자료에서 예측된 값 t는 정답으로 주어진 값
    # x (5000, 12)
    y = predict(network, x)
    # y (5000, output_size)
    # t (5000, 10) : one-hot-encoding이니까
    # 정확도는 어떻게 비교해야 할까요~ 먼저 생각해보깅
    
    # 예측된 값과 one_hot_encoding으로 된 y_train값을 비교하여 정확도를 출력

    return accuracy


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    # 간단한 버전, 해보고 안되면 이전껄로 바꿔요
    x = x - np.max(x, axis=-1) # axis -1 means last!
    y = np.exp(x) / np.sum(np.exp(x), axis=-1)
    return y

if __name__ == '__main__':
    filename = 'SimpleNetData.csv' # change to absolute path
    x_train, y_train = load_csv(filename)
    y_train = one_hot_encoding(y_train)

    network = init_network(len(x_train[1]), 100, 10)

    accuracy = accuracy(x_train, y_train)

    print (accuracy)