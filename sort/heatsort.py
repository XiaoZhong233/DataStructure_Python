def swap(tree,i,j):
	temp = tree[i]
	tree[i] = tree[j]
	tree[j] = temp

# 调整堆
def heapify(tree,i):
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
		swap(tree,max,i)
		heapify(tree,max)

# 构造堆
def build_heap(tree):
	last_node = len(tree)-1
	parent = int((last_node - 1) / 2)
	for i in range(parent,-1,-1):
		heapify(tree,i)

# 堆排序
def heap_sort(tree):
	build_heap(tree)
	result = []
	for i in range(len(tree)-1,-1,-1):
		# 交换根节点与最后一个节点,砍断最后一个节点，重新调整堆
		swap(tree,i,0)
		result.append(tree.pop())
		heapify(tree,0)
	return result
	


if __name__ == "__main__":
	tree = [2,5,3,1,10,4]
	result = heap_sort(tree)

	for node in result:
		print(node.__str__(),end = " ")




