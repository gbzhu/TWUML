def sign(x):
    return 1 if x > 0 else -1


if __name__ == '__main__':
    data_file = open("data/hw1_15_train.dat")
    for i in data_file.readlines():
        line = "1 " + i.replace("\t", " ")
        pass