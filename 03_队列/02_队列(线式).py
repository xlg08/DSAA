class Array:
    def __init__(self, size=4):
        self.__size = size      # 记录容器的大小
        self.__item = [None] * size  # 分配空间
        self.__length = 0

    # 向数组中添加元素
    def __setitem__(self, key, value):
        self.__item[key] = value
        self.__length += 1

    # 从数组中获得元素
    def __getitem__(self, key):
        return self.__item[key]

    # 返回数组的大小
    def __len__(self):
        return self.__length

    def __iter__(self):
        for value in self.__item:
            yield value

class Queue:
    def __init__(self, size = 4):
        self.item = Array(size)
        self.size = size
        self.head = 0
        self.end = 0

    def put(self, value):
        self.item[self.head % self.size] = value    # 队列长度固定，超出长度会覆盖之前的
        # print(self.head)
        # print(self.head % self.size)
        self.head += 1

    def pop(self):
        temp = self.item[self.end % self.size]
        self.end += 1
        return temp

if __name__ == '__main__':
    q = Queue()
    q.put("张三")
    q.put("李四")
    q.put("王五")
    q.put("赵六")
    q.put("钱七")

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


