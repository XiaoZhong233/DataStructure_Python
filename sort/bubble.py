# coding:utf-8
# 交换数据元素
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# 一次冒泡,把最大的元素换到后面
def bubble(arr, n):
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            swap(arr, i, i + 1)


def bubbleSort(arr):
    for i in range(len(arr), 0, -1):
        bubble(arr, i)


# 一次冒泡，把最小的元素换到后面
def bubble1(arr, n):
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            swap(arr, i, i + 1)


def bubbleSort1(arr):
    for i in range(len(arr), 0, -1):
        bubble1(arr, i)


# 改进版的冒泡排序，设置标志位标志是否发生交换，未发生交换则排序结束
def bubble2(arr, n):
    flag = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            swap(arr, i, i + 1)
            flag = True
    return flag


def bubbleSort2(arr):
    for i in range(len(arr), 0, -1):
        if not bubble2(arr, i):
            break


if __name__ == '__main__':
    data = [3, 4, 6, 2, 8]
    print("升序冒泡")
    bubbleSort(data)
    print(data)
    print("降序冒泡")
    bubbleSort1(data)
    print(data)
    print("改进版冒泡")
    bubbleSort2(data)
    print(data)
