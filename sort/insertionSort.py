# coding:utf-8
# 一趟插入排序
def insert(arr, n):
    key = arr[n]
    i = n
    while arr[i - 1] > key:
        arr[i] = arr[i - 1]
        i -= 1
        if i == 0:
            break
        pass
    arr[i] = key


def insertionSort(arr):
    # 从第二个元素开始插入排序
    for i in range(1, len(arr), 1):
        insert(arr, i)


if __name__ == '__main__':
    data = [3, 7, 4, 10, 12, 7]
    insertionSort(data)
    print(data)
