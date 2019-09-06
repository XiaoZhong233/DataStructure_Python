# coding:utf-8
# 交换数据元素
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def findMaxPos(arr, n):
    if not arr:
        return
    max = arr[0]
    pos = 0
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
            pos = i
    return pos


def selectionSort(arr):
    for i in range(len(data), 1, -1):
        pos = findMaxPos(arr, i)
        swap(arr, i - 1, pos)


if __name__ == '__main__':
    data = [3, 4, 6, 1, 9, 2]
    selectionSort(data)
    print(data)
