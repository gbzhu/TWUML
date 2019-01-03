import numpy as np
from P15 import sign
from P15 import init_data
import random
import matplotlib.pyplot as plt


def cul_error(data, w, n):
    """
    计算当前 W 所产生的 Error
    :param data: D
    :param w:
    :param n: 数据的维度
    :return:
    """
    count = 0
    for i in data:
        if sign(i[:n].dot(w)) * i[-1] < 0:
            count += 1
    return count


def pocketPLA(data, d, n, k, max_num):
    """
    :param data: D
    :param d: 数据维度
    :param n: 数据的组数
    :param k: 步长
    :param max_num: 最大更新次数
    :return:
    """
    w = np.zeros(d)
    w0 = np.zeros(d)
    time = 0
    index = 0
    error = cul_error(data=data, w=w, n=d)
    if error == 0:
        pass
    else:
        while time < max_num and error > 0:
            i = data[index]
            if sign(i[:d].dot(w)) * i[-1] < 0:
                w += i[:d] * i[-1] * k
                time += 1
            temp_error = cul_error(data=data, w=w, n=d)
            if temp_error < error:
                w0 = w
                error = temp_error
            index += 1
            if index >= n:
                index %= n
    return w0, error


if __name__ == '__main__':
    train_data = init_data(path="data/hw1_18_train.dat")
    d_data = len(train_data[0]) - 1
    n_data = len(train_data)
    num = 50
    k = 1

    x = []
    for i in range(2000):
        random.shuffle(train_data)
        error = pocketPLA(train_data, d_data, n_data, k, num)[1]
        if i % 100 == 0:
            print(i)
        x.append(error)
    plt.hist(x, normed=True)
    plt.xlabel("Error")
    plt.title("Average Error : " + str(sum(x) / 2000))
    plt.show()
