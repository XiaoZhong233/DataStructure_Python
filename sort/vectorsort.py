# coding = "utf-8"
import sys

sys.path.append('../tool')
import TimeCalculator
import BitSet
import numpy as np


def generate_data(n):
    return np.random.randint(low=0, high=n, size=n)

# 写成txt文件
def wirte_data(n):
    data = generate_data(n)
    np.savetxt('./data.txt', X=data, fmt="%d",delimiter=" ", newline = " ")

# 写成二进制文件
def wirte_data2(n):
    data = generate_data(n)
    np.save(file ='./data', arr = data, )

def load_data2(file = './data.npy'):
    return np.load(file)


# 对n（n<=1000000）个小于n的正整数序列进行排序
# 时间在10s以内
# 空间占用小于1MB
@TimeCalculator.display_time
def vertorsort(data, n=1000000):
    bitset = BitSet.BitSet(n)
    # 初始化位图,模拟从I/O读入数据
    for i in data:
        bitset.set(i)
    result = []
    # 输出位图排序结果,模拟向I/0写入数据
    print("空间大小占用:")
    print(str(sys.getsizeof(bitset)) + "Byte")
    for i in range(bitset.size()):
        if bitset.test(i):
            result.append(i)
    return result
    pass


if __name__ == '__main__':
    # 模拟100万个100万内的数据
    wirte_data2(10**6)
    # 模拟从磁盘中读取数据
    data = load_data2()
    # 模拟向I/O输出排序结果
    result = vertorsort(data, 10**6)
    np.savetxt('./datasort.txt', X=result, fmt="%d",delimiter=" ", newline = " ")
    # print(result)
