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
            # node.prev = self.root       # 设置新节点的 上一个节点               为root
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


if __name__ == '__main__':

    link = DoubleLinkedList()
    link.append("张三")
    link.append("李四")
    link.append_first("王五")
    link.append("赵六")

    for v in link:
        print(v)

    print("*"*50)

    for v in link.revers_iter():
        print(v)