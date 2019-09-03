# 二分查找
def binary_search(data, key):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if data[mid] == key:
            return mid
        elif key < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
        pass
    return -1


# 二分查找（递归）
def binary_search2(data, key):
    if not data or not key:
        return False
    if len(data) > 0:
        mid = (len(data) - 1) // 2
        if key == data[mid]:
            return True
        elif key < data[mid]:
            return binary_search2(data[:mid], key)
        else:
            return binary_search2(data[mid + 1:], key)
    return False


if __name__ == '__main__':
    data = [5, 16, 20, 27, 30, 36, 44, 55, 60, 71, 76]
    # result = binary_search(data,30)
    # print(result)
    # print(data[result])

    result2 = binary_search2(data, 4)
    print(result2)

    # result2 = binary_search2(data, 76)
    # print(result2)
