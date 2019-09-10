# coding = 'utf-8'
import random
import sys

sys.path.append('../tool')
import TimeCalculator
import numpy as np


# 一趟快排
def partSort(data, low, high):
    pivotkey = data[low]  # 子表的第一个元素作为枢纽记录
    while low < high:
        while low < high and data[high] >= pivotkey:
            high = high - 1
            pass
        data[low] = data[high]  # 将比枢纽元素小的元素移动至low处
        while low < high and data[low] <= pivotkey:
            low = low + 1
            pass
        data[high] = data[low]
        pass
    data[low] = pivotkey  # 枢纽记录更新
    return low


# 递归排序序列
def qsort(data, low, high):
    if low < high:
        pivotloc = partSort(data, low, high)  # 将data一分为二，并记录下枢纽的位置
        qsort(data, low, pivotloc - 1)  # 左子表进行递归排序
        qsort(data, pivotloc + 1, high)


def quicksort(data):
    low, high = 0, len(data) - 1
    qsort(data, low, high)


# 快排实现2（python开挂版）
def quicksort2(data):
    if len(data) < 2:
        return data
    else:
        pivotloc = 0
        pivotkey = data[pivotloc]
        less_part = [i for i in data[pivotloc + 1:] if i <= pivotkey]
        great_part = [i for i in data[pivotloc + 1:] if i > pivotkey]
        return quicksort2(less_part) + [pivotkey] + quicksort2(great_part)


# 快排实现非递归
def quicksort3(data):
    low, high = 0, len(data) - 1
    stack = []
    pivotloc = partSort(data, low, high)
    # 入栈
    if pivotloc > low + 1:
        stack.append(low)
        stack.append(pivotloc - 1)
    elif pivotloc < high - 1:
        stack.append(pivotloc + 1)
        stack.append(high)

    # 出栈
    while not stack:
        high = stack.pop()
        low = stack.pop()
        pivotloc = partSort(data, low, high)
        if pivotloc > low + 1:
            stack.append(low)
            stack.append(pivotloc - 1)
        elif pivotloc < high - 1:
            stack.append(pivotloc + 1)
            stack.append(high)
        pass


def generate_data(n):
    return np.random.randint(low=0, high=n, size=n)


# 测试传统递归快排
@TimeCalculator.display_time
def testQuicksort(n):
    seq = generate_data(n)
    quicksort(seq)
    # print(seq)


# 测试python简化版
@TimeCalculator.display_time
def testQuicksort2(n):
    seq = generate_data(n)
    seq = quicksort2(seq)
    # print(seq)


# 测试非递归算法
@TimeCalculator.display_time
def testQuicksort3(n):
    seq = generate_data(n)
    quicksort3(seq)


if __name__ == '__main__':
    # testQuicksort(10 ** 4)
    # testQuicksort2(10 ** 4)
    testQuicksort3(10 ** 6)
    print("非递归快排最好")
