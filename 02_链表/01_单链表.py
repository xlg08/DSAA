class Node:
    def __init__(self, value=None, next=None):
        self.value = value      # 该结点的值
        self.next = next    # 该结点指向的下一个节点
    def __str__(self):
        return 'Node:{}'.format(self.value)

class LinkedList:
    def __init__(self,):
        self.root = Node()      # 链表有一个根节点
        self.size = 0       # 链表的数据有多大
        # self.end 是在增加新数据时，将新数据的索引(地址)与谁关联
        # self.end指向的是最后一个节点
        self.end = None


    def append(self, value):    # 在末尾增加
        node = Node(value)      # 将增加的值实例化为一个node
        # 判断是否已经有数据了
        if not self.end:   # 如果是一个空链表，没有节点
            self.root.next = node       # 将新节点挂到root根节点后面
            # self.next = node
        else:
            self.end.next = node       # 将新节点挂到最后一个节点上
            # self.next = node
        self.end = node
        self.size += 1

    def append_first(self, value):  # 在头部增加
        node = Node(value)
        if not self.end:
            self.root.next = node
            self.end = node
        else:
            temp = self.root.next       # 获取原来 root 后面的节点
            self.root.next = node       # 将新的节点挂载到root上
            node.next = temp
        self.size += 1

    def __iter__(self):
        current = self.root.next
        # if not current:
        #     yield current.value
        # else:
        #     pass
        if current:
            while current is not self.end:     # 判断该节点的下一个节点不为空时循环
                # yield current.value
                # yield的函数则返回一个可迭代的 generator（生成器）对象
                yield current
                current = current.next
            # yield current.value
            yield current

    def find(self, value):
        for n in self.__iter__():
            if n.value == value:
                return n

    def find_count(self, value):
        count = 0
        for n in self.__iter__():
            if n.value == value:
                count += 1
        return count

    def remove(self, value):
        # prev指的是 需要删除的节点的上一个节点，即需要断开的节点的上一个节点，需要用它重指向需要断开的节点的下一个节点，否则链会断开
        prev = self.root
        for n in self.__iter__():
            if n.value == value:
                if n == self.end:
                    prev.next = None
                    self.end = prev
                prev.next = n.next
                del n
                self.size -= 1
                return True
            prev = n
    def remove_all(self, value):
        prev = self.root
        for n in self.__iter__():
            if n.value == value:
                if n == self.end:
                    prev.next = None
                    self.end = prev
                prev.next = n.next
                del n
                self.size -= 1
                continue
            prev = n

if __name__ == '__main__':
    link = LinkedList()
    link.append("1哈哈")
    link.append("2拉拉")
    link.append("2拉拉")
    link.append("2拉拉")
    link.append("2拉拉")
    link.append_first("3哇哇")
    print("删除之前")
    for node in link:
        print(node)

    print("删除之后")
    link.remove_all("2拉拉")
    for node in link:
        print(node)

    # print(link.find("2拉拉"))
    # print(link.find_count("2拉拉"))




