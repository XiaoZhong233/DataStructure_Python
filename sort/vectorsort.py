# coding = "utf-8"
import sys

sys.path.append('../tool')
import TimeCalculator
import BitSet
import numpy as np


def generate_data(n):
    return np.random.randint(low=0, high=n, size=n)


# 对n（n<=1000000）个小于n的正整数序列进行排序
# 时间在10s以内
# 空间占用小于1MB
@TimeCalculator.display_time
def vertorsort(data, n = 1000000):
    bitset = BitSet.BitSet(n)
    # 初始化位图
    for i in data:
        bitset.set(i)
    result = []
    # 输出位图排序结果
    print("空间大小占用:")
    print(str(sys.getsizeof(bitset)) + "Byte")
    for i in range(bitset.size()):
        if bitset.test(i):
            result.append(i)
    return result
    pass


if __name__ == '__main__':
    data = generate_data(1000000)
    result = vertorsort(data, len(data))
    print(result)
    # data.sort()
    # print(data)
