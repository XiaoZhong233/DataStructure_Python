# coding=utf-8
import tool.TimeCalculator as time

class Hash:
    def __init__(self, size):
        self.size = size
        self.strategy = lambda x: x % self.size
        self.hashSet = [None] * size

    def Secondary_detection(self, hashCode, offset):
        return self.strategy((hashCode + offset) ** 2)

    def Linear_detection(self, hashCode, offset):
        return self.strategy(hashCode + offset)

    @time.display_time
    def search(self, key):
        hashCode = self.strategy(key)
        if self.hashSet[hashCode] is None:
            return None
        elif self.hashSet[hashCode] == key:
            return hashCode
        else:
            for i in range(1, self.size):
                # 线性探测法
                print("元素%s在第%s位冲突" % (key, hashCode))
                hashCode = self.Linear_detection(hashCode, i)
                if self.hashSet[hashCode] == key:
                    return hashCode
                pass
            return None

    def insert(self, key):
        hashCode = self.strategy(key)
        if self.hashSet[hashCode] is None:
            self.hashSet[hashCode] = key
        else:
            for i in range(1, self.size):
                hashCode_next = self.Linear_detection(hashCode, i)
                print("元素%s插入冲突，尝试插入第%s位" % (key, hashCode_next))
                if self.hashSet[hashCode_next] is None:
                    self.hashSet[hashCode_next] = key
                    break
            print("HASH表已满，无法插入元素%s" % key)
            return -1

    def printHashSet(self):
        print(self.hashSet)


if __name__ == '__main__':
    hash = Hash(10)
    for i in range(11):
        hash.insert(i)
    hash.printHashSet()

    print()
    print("查找key=9的位置")
    print("index=%s" % hash.search(9))

    print()
    print("\n查找key=10的位置")
    print("index=%s" % hash.search(10))
