# codint = utf-8
import sys

sys.path.append('../tool')
import TimeCalculator
import numpy as np


def shellInsert(data, dk):
    for i in range(dk, len(data), 1):
        if data[i - dk] > data[i]:
            # 保存需要移动的元素
            key = data[i]
            # i-dk前面的元素后移
            j = i - dk
            while j >= 0 and key < data[j]:
                data[j + dk] = data[j]
                j = j - dk
                pass
            # 移动的元素插入到正确的位置
            data[j + dk] = key


@TimeCalculator.display_time
def shellSort(data, increment):
    for i in increment:
        shellInsert(data, i)


def generate_data(n):
    return np.random.randint(low=0, high=n, size=n)


def generate_increment(n):
    increment = []
    for i in range(n - 1, -1, -1):
        if TimeCalculator.is_prime(i):
            increment.append(i)
    increment[len(increment) - 1] = 1
    return increment


if __name__ == '__main__':
    data = generate_data(10 ** 2)
    increment = generate_increment(len(data))
    shellSort(data, increment)
    print(data)
    # shellSort(data, )
    # print(data)
