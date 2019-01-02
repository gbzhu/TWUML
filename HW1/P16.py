import P15
import random
import matplotlib.pyplot as plt

data = P15.init_data(path=P15.FILE_PATH)
# 数据维度
d_data = len(data[0]) - 1
# 数据的组数
l_data = len(data)

times = []

for i in range(2000):
    # print(i)
    random.shuffle(data)
    times.append(P15.PLA(data=data, d=d_data, l=l_data)[1])
plt.hist(times, normed=True)
plt.xlabel("Number of Iterations")
plt.title("Average run times : " + str(sum(times) / 2000))
plt.show()
