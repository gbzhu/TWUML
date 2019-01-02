import numpy as np
from P15 import sign


def cul_error(data, w, n):
    count = 0
    for i in data:
        if sign(i[:n].dot(w)) * i[-1] < 0:
            count += 1
    return count


def PocketPLA(data, n):
    w0 = np.zeros(n)
    # 记录迭代次数
    time = 0
    error = cul_error(data=data, w=w0, n=n)
    if error == 0:
        pass
    else:
        for i in data:
            pass
