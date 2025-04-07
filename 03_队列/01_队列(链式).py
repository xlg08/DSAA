"""
    线性队列、链式队列：   先进先出  头进尾出
            双端队列：   可头进头出、可尾进尾出、可头进尾出、可尾进头出
            队列类似于排队

            栈：        先进后出 头进头出
            栈类似于压子弹


"""

class Node:
    def __init__(self, value=None,prev=None,next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"Node: {self.value}"

class DoubleLinkedList:
    def __init__(self):
        self.root = Node()
        self.size = 0
        self.end = None

    def append(self, value):
        node = Node(value)      # 封装节点对象
        # 判断是否已经有数据
        if not self.end:    # 如果最后一个节点没有元素
            self.root.next = node   # 将root的下一个节点 设置为新的node节点
            node.prev = self.root   # 设置新节点的上一个节点时root
            # self.end = node  # 更新最后一个节点为新加的节点
        else:
            self.end.next = node    # 将原来的最后节点的下一个节点，设置为新的node节点
            node.prev = self.end    # 设置新的node节点的上一个节点为最后一个节点
            # self.end = node     # 更新最后一个节点为新加的节点
        self.end = node  # 更新最后一个节点为新加的节点
        self.size += 1

    def append_first(self, value):
        node = Node(value)
        # 判断是否有数据
        if not self.end:    # 如果没有数据
            # self.root.next = node  # 将root的下一个节点 设置为新的node节点
            # node.prev = self.root  # 设置新节点的上一个节点是root
            self.end = node  # 更新最后一个节点为新加的节点
        else:
            temp = self.root.next       # 保存原来的第一个节点
            # node.prev = self.root       # 设置新节点的 上一个节点 为root
            node.next = temp        # 设置新节点的下一个节点为原来的 第一个节点
            # self.root.next = node # 将root的下一个节点 设置为新的node节点
            temp.prev = node    # 更新原来的第一个节点的上一个节点位置为 新的node节点
        node.prev = self.root  # 设置新节点的上一个节点时root
        self.root.next = node  # 将root的下一个节点 设置为新的node节点
        self.size += 1

    def __iter__(self):
        current = self.root.next
        if current:
            while current is not self.end:
                # yield current.value
                yield current
                current = current.next
            # yield current.value
            yield current

    # 从后进行遍历
    def revers_iter(self):
        current = self.end      # 获取最后一个节点
        if current:
            while current is not self.root:
                yield current
                current = current.prev

    def remove_first(self):
        if self.end:
            temp = self.root.next       # 获取第一个节点
            self.root.next = temp.next      # 设置链表的第二个节点为 root 的下一个节点
            if temp.next:       # 判断下一个节点是否仍然是一个节点，而不是None
                temp.next.prev = self.root     # 设置第一个节点的上一个节点为root
            return temp

class Queue():
    def __init__(self, size=4):
        # 链式队列这种数据结构采用链表这种容器存储数据
        self.item = DoubleLinkedList()
        self.size = size
        self.length = 0

    def put(self, value):
        self.item.append(value)
        self.length += 1

    def pop(self):

        self.length -= 1

        return self.item.remove_first()

    def empty(self):
        pass

if __name__ == '__main__':
        q = Queue()
        q.put("1哈哈")
        q.put("2拉拉")
        q.put("3哈哈")
        q.put("3哈哈")
        q.put("3哈哈")
        q.put("3哈哈")

        # for _ in q.item:
        #     print(_)

        print(q.pop())
        print(q.pop())
        print(q.pop())