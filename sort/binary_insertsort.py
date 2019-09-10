# coding = 'utf-8'
# 折半插入排序，直接插入排序的优化，基本思想就是将原来直接插入排序的顺序查找插入位置，改为二叉查找插入位置
# 稳定排序，适合初始元素较多且无序的情况
import sys
sys.path.append('../tool')
import random
import TimeCalculator as time


@time.display_time
def binary_insertsort(data):
	for i in range(1, len(data), 1):
		key = data[i]  # 待插入的记录
		low, high = 0, i - 1  # 折半查找区间初值,也就是待插入元素的前面的元素的区间
		while low <= high:
			m = int((low + high) / 2)
			if data[m] > key:
				high = m - 1  # 插入点在左子表中
			else:
				low = m + 1  # 插入点在右子表中
			pass
		# 记录后移
		j = i - 1
		while j >= high + 1:
			data[j + 1] = data[j]
			j = j - 1
			pass
		# 待插入记录插入至正确位置
		data[high + 1] = key


if __name__ == '__main__':
	data = list(range(10**2))
	datacopy = data.copy()
	random.shuffle(data)
	binary_insertsort(data)
	assert data == sorted(datacopy)
	print(data)
