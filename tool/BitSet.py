# coding='utf-8'
import array

class BitSet(object):
	def __init__(self, capacity):
		#"B"类型相当于 C 语言的 unsigned char， 即占用1byte（8位），所以size大小设置为8，一个数占一个字节
		self.unit_size = 8
		self.unit_count = int((capacity + self.unit_size - 1) / self.unit_size)
		self.capacity = capacity
		self.arr = array.array("B", [0] * self.unit_count)
		pass

	# 是否存在为1的位
	def any(self):
		for a in self.arr:
			if a != 0:
				return True
		return False

	def all(self):
		#是否所有位都为 1， 即是否存在置为 0 的位
		t = (1 << self.unit_size) - 1
		for a in self.arr:
			if (a & t) != t:
				return False
		return True

	def none(self):
		#是否所有位都为 0，即是否不存在置为 1 的位
		for a in self.arr:
			if a != 0:
				return False
			return True

	def count(self):
		# 1 的位的个数
		c = 0
		for a in self.arr:
			while a > 0:
				if a & 1:
					c+=1
				a = a>>1
				pass
		return c

	def size(self):
		#所有位的个数
		return self.unit_count * self.unit_size


	def get(self, pos):
		#获取第 pos 位的值
		index = int(pos / self.unit_size)
		offset = (self.unit_size - (pos - index * self.unit_size) - 1) % self.unit_size
		return (self.arr[index] >> offset) & 1	

	def test(self, pos):
		#判断第 pos 位的值是否为 1
		if self.get(pos):
			return True
		return False

	def set(self, pos = -1):
		#设置第 pos 位的值为 1，若 pos 为 -1， 则所有位都置为 1
		if pos >= 0:
			index = int(pos / self.unit_size)
			offset = (self.unit_size - (pos - index * self.unit_size) - 1) % self.unit_size
			self.arr[index] = (self.arr[index]) | (1 << offset)
		else:
			t = (1 << self.unit_size) - 1
			for i in range(self.unit_count):
				self.arr[i] = self.arr[i] | t

	def reset(self, pos = -1):
		#设置第 pos 位的值为 0，若 pos 为 -1， 则所有位都置为 0
		if pos >= 0:
			index = int(pos / self.unit_size)
			offset = (self.unit_size - (pos - index * self.unit_size) - 1) % self.unit_size
			x = (1 << offset)
			self.arr[index] = (self.arr[index]) & (~x)
		else:
			for i in range(self.unit_count):
				self.arr[i] = 0

	def flip(self, pos = -1):
		#把第 pos 位的值取反，若 pos 为 -1， 则所有位都取反
		if pos >= 0:
			if self.get(pos):
				self.reset(pos)
			else:
				self.set(pos)
		else:
			for i in range(self.unit_count):
				self.arr[i] = ~self.arr[i] + (1 << self.unit_size)

	def binstr(self):
		b = ''
		for a in self.arr:
			t = bin(a)
			b += "0" * (self.unit_size - len(t) + 2) + t + ","
		return "[" + b.replace("0b", "").strip(",") + "]"


	def show(self):
		return self.arr

if __name__ == '__main__':
	bitSet = BitSet(32)
	bitSet.set()
	print(bitSet.binstr())
	print(bitSet.count())

