'''
    @User: LG
    @Auther: http://www.xlonggang.cn
    @Date: 2025/4/9 0009 22:32 
    @Description: 
    @Project ：数据结构 
    @File    ：01_最大堆的实现.py
    @version: 1.0
'''


class Array:
    def __init__(self, size=4):
        self.__size = size  # 记录容器的大小
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


class Heap:
    def __init__(self):
        self.item = Array(8)
        self.count = 0

    # 添加的节点
    def add(self, value):
        self.item[self.count] = value     # 将该值添加到最后一个位置
        self.siftup(self.count)
        self.count += 1

    # 添加新节点时，与父结点进行比较，如果比父节点大，实现换值效果
    def siftup(self, index):
        if index > 0:  # 当不是根节点就进行比较
            parent = (index - 1) // 2  # 找到该节点的父节点的索引
            if self.item[index] > self.item[parent]:  # 如果当前节点比父节点小则进行交换
                self.item[index], self.item[parent] = self.item[parent], self.item[index]
                # 当前元素与父节点交换完之后，则将当前节点再向上进行比较，只到不比对应的父节点大，或已经成为根节点
                self.siftup(parent)

    # 取出一个节点，并返回该结点的值
    def pop(self, index=0):         # 默认取出根节点，即：最大的元素
        if self.count <= 0:  # 如果当前堆的元素为0个，则返回空
            return None
        else:
            value = self.item[index]   # 获取要取出的当前位置节点的值
            self.count -= 1  # 将堆中的元素个数减一
            self.item[index] = self.item[self.count]  # 将最后一个节点移到当前位置
            self.item[self.count] = None  # 将最后一个节点置空
            self.siftdown(index)  # 去掉该元素
            return value

    def siftdown(self, index):
        # 获取该节点的左子节点和右子节点
        left = index * 2 + 1
        right = index * 2 + 2

        largest = index         # 默认当前位置上的节点是最大的元素

        # 判断三个节点中最大的节点的索引
        if right < self.count:  # 判断是否存在右子节点
            # 找出当前位置节点与左子节点和右子节点这三个节点中最大的节点
            if self.item[right] > self.item[largest] and self.item[right] > self.item[left]:
                # 当右子节点为最大的节点时
                largest = right
            # elif self.item[right] > self.item[largest] and self.item[right] < self.item[left]:
            elif self.item[largest] < self.item[right] < self.item[left]:
                # 当左子节点为最大的节点时
                largest = left
            # elif self.item[right] < self.item[largest] and self.item[left] > self.item[largest]:
            elif self.item[right] < self.item[largest] < self.item[left]:
                # 当左子节点为最大的节点时
                largest = left
        elif left < self.count:  # 当前没有右子节点,判断是否有左子节点
            if self.item[left] > self.item[largest]:
                largest = left

        # 如果最大值的索引改变了，则当前位置元素不是最大的，则需要与左或子节点的最大的元素进行交换
        if largest != index:
            self.item[index], self.item[largest] = self.item[largest], self.item[index]
            # 将重新换到左或右子节点的元素，作为新的父节点，再向下进行比较的
            self.siftdown(largest)


if __name__ == '__main__':
    heap = Heap()
    heap.add(10)
    heap.add(15)
    heap.add(20)
    heap.add(14)
    heap.add(30)

    for i in heap.item:
        if i:
            print(i)

    print("♥" * 50)
    print(heap.pop(1))
    print("♥" * 50)

    for i in heap.item:
        if i:
            print(i)


    # print(heap.pop())
    # print(heap.pop())
    # print(heap.pop())
