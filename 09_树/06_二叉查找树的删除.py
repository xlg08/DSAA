node_list = [
    {'data': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'data': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'data': 4, 'left': 1, 'right': None, 'is_root': False},
    {'data': 1, 'left': None, 'right': None, 'is_root': False},
    {'data': 41, 'left': 29, 'right': None, 'is_root': False},
    {'data': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'data': 23, 'left': None, 'right': None, 'is_root': False},
    {'data': 37, 'left': None, 'right': None, 'is_root': False},
    {'data': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'data': 71, 'left': None, 'right': 84, 'is_root': False},
    {'data': 100, 'left': None, 'right': None, 'is_root': False},
    {'data': 84, 'left': None, 'right': None, 'is_root': False},
]


class Node:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def __str__(self):
        return f"数据是：{self.data}"


class Tree:
    def __init__(self, root=None):
        self.root = root

    def init_data(self, datas):
        node_dict = {}
        for d in datas:
            node = Node(d['data'], d['left'], d['right'])
            node_dict[d['data']] = node
        for d in datas:
            node = node_dict[d['data']]
            if node.left:
                node.left = node_dict[node.left]
            if node.right:
                node.right = node_dict[node.right]
            if d['is_root']:
                self.root = node

    def search(self, subtree, value):
        if subtree is None:
            return None
        elif subtree.data > value:
            return self.search(subtree.left, value)
        elif subtree.data < value:
            return self.search(subtree.right, value)
        else:
            return subtree

    def get_min(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self.get_min(subtree.left)

    def insert_data(self, subtree, value):
        if subtree is None:

            subtree = Node(value)

        elif subtree.data > value:
            subtree.left = self.insert_data(subtree.left, value)
        else:
            subtree.right = self.insert_data(subtree.right, value)

        return subtree

    def add(self, value):

        node = self.search(self.root, value)
        if node:
            return False
        else:
            self.root = self.insert_data(self.root, value)
            return True

    # 实际删除节点操作
    def remove_node(self, subtree, value):
        if subtree is None:         # 此处判断不知判断传入的父节点，还有在递归删除时的节点
            return None
        elif subtree.data > value:      # 如果当前结点的值大于要删除的值，则去左子节点寻找删除
            subtree.left = self.remove_node(subtree.left, value)       # 通过左节点进行查找删除
            return subtree.left
        elif subtree.data < value:      # 如果当前结点的值小于要删除的值，则去右子节点寻找删除
            subtree.right = self.remove_node(subtree.right, value)
        else:           # 此处当前结点的值就是要删除的值
            # 找到数据节点  ： 1.当前为叶子节点  2.有一个孩子  3.有两个孩子    三种情况
            if subtree.left is None and subtree.right is None:      # 为叶子节点时
                return None
            elif subtree.left is None or subtree.right is None:     # 有一个孩子时，当左或右子节点任意有一个不为空
                if subtree.left is None:
                    return subtree.left
                else:
                    return subtree.right
            else:           # 有两个孩子时，需要找到最小的值
                # 从右节点中找到最小的值
                #   因为右节点中的值比左节点中的都大，所以找到右节点的最小值，作为新的父节点，可以保证大于左节点小于右节点
                node = self.get_min(subtree.right)
                subtree.data = node.data
                subtree.right = self.remove_node(subtree.right, node.data)
                return subtree

    def remove(self, value):
        if self.search:      # 先查找值是否在树中存在
            self.remove_node(self.root, value)

if __name__ == '__main__':
    tree = Tree()
    # tree.init_data(node_list)

    tree.add(60)
    tree.add(12)
    tree.add(90)
    tree.add(4)
    tree.add(41)
    tree.add(71)
    tree.add(100)
    tree.add(1)
    tree.add(29)
    tree.add(84)
    tree.add(23)
    tree.add(37)

    print(tree.root.data)
    print(tree.root.left)
    tree.remove(12)
    print(tree.root.data)
    print(tree.root.left)


