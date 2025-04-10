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


class Heap:
    def __init__(self):
        self.item = Array(8)
        self.count = 0

    # 添加的节点
    def add(self, value):
        self.item[self.count] = value
        self.siftup(self.count)
        self.count += 1


    # 添加新节点时，与父结点进行比较，如果比父节点大，实现换值效果
    def siftup(self, index):
        if index > 0:       # 当不是根节点就进行比较
            parent = (index-1)//2           # 找到该节点的父节点的索引
            if self.item[index] > self.item[parent]:        # 如果当前节点比父节点小则进行交换
                self.item[index], self.item[parent] = self.item[parent], self.item[index]
                # 当前元素与父节点交换完之后，则将当前节点再向上进行比较，只到不比对应的父节点大，或已经成为根节点
                self.siftup(parent)



if __name__ == '__main__':
    heap = Heap()
    heap.add(10)
    heap.add(15)
    heap.add(20)
    heap.add(14)

    for i in heap.item:
        if i:
            print(i)
