# coding:utf-8
# 交换数据元素
def swap(tree, i, j):
    temp = tree[i]
    tree[i] = tree[j]
    tree[j] = temp


# 调整堆，调整为大根堆
def heapify(tree, i):
    if i >= len(tree):
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    max = i
    if c1 < len(tree) and tree[c1] > tree[max]:
        max = c1
    if c2 < len(tree) and tree[c2] > tree[max]:
        max = c2
    if max != i:
        swap(tree, max, i)
        heapify(tree, max)


# 构造堆
def build_heap(tree):
    last_node = len(tree) - 1
    parent = int((last_node - 1) / 2)
    for i in range(parent, -1, -1):
        heapify(tree, i)


# 堆排序.大根堆，降序
def heap_sort(tree):
    build_heap(tree)
    result = []
    for i in range(len(tree) - 1, -1, -1):
        # 交换根节点与最后一个节点,砍断最后一个节点，重新调整堆
        swap(tree, i, 0)
        result.append(tree.pop())
        heapify(tree, 0)
    return result


# 调整堆，调整为小根堆
def heapify1(tree, i):
    if i >= len(tree):
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    min = i
    if c1 < len(tree) and tree[c1] < tree[min]:
        min = c1
    if c2 < len(tree) and tree[c2] < tree[min]:
        min = c2
    if min != i:
        swap(tree, min, i)
        heapify(tree, min)


# 构造小根堆
def build_heap1(tree):
    last_node = len(tree) - 1
    parent = int((last_node - 1) / 2)
    for i in range(parent, -1, -1):
        heapify1(tree, i)


# 堆排序.小根堆，升序
def heap_sort1(tree):
    build_heap1(tree)
    result = []
    for i in range(len(tree) - 1, -1, -1):
        # 交换根节点与最后一个节点,砍断最后一个节点，重新调整堆
        swap(tree, i, 0)
        result.append(tree.pop())
        heapify1(tree, 0)
    return result


if __name__ == "__main__":
    tree = [2, 5, 3, 1, 10, 4]
    print("原始数据：")
    print(tree)
    result = heap_sort(tree)
    print("大根堆排序：")
    print(result)

    # 小根堆测试用例
    tree = [345, 312, 65, 765, 143, 564]
    print("原始数据：")
    print(tree)
    result = heap_sort1(tree)
    print("小根堆排序：")
    print(result)
