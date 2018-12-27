import numpy as np


def init_data(path: str):
    data = []
    data_file = open(path)
    for i in data_file.readlines():
        # add x0 = 1
        line = "1 " + i.replace("\t", " ").replace("\n", "")
        line_array = line.split(" ")
        data.append(np.array(list(map(float, line_array))))
    return data


def sign(x):
    return 1 if x > 0 else -1


def judge(data, w, d):
    for x in data:
        if sign(np.dot(x[:d], w)) * x[-1] < 0:
            return True
    return False


def PLA(data, d, l):
    w = np.zeros(d)
    index = 0
    time = 0
    while judge(data=data, w=w, d=d):
        x = data[index]
        if sign(np.dot(x[:d], w)) * x[-1] < 0:
            w += x[:d] * x[-1]
            time += 1
        index += 1
        if index >= l:
            index %= l

    return w, time, index


if __name__ == '__main__':
    file_path = "data/hw1_15_train.dat"
    data = init_data(path=file_path)
    # 数据维度
    d_data = len(data[0]) - 1
    # 数据的组数
    l_data = len(data)
    w, t, i = PLA(data=data, d=d_data, l=l_data)
    print(w, t, i)
