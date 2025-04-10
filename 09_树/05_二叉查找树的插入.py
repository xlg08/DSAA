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

    # 实际插入操作，该方法主要考虑插入的操作，规则，逻辑
    def insert_data(self, subtree, value):
        if subtree is None:
            # 如果传入的该节点为空，没有数据的话，则可以直接将要插入的数据封装成的节点赋值给该节点
            subtree = Node(value)

        elif subtree.data > value:      # 如果要插入的数据比该节点上的数据小的话，则向该节点的左子树去寻找插入位置
            subtree.left = self.insert_data(subtree.left, value)
        else:       # 如果要插入的数据比该节点上的数据大的话，则向该节点的右子树去寻找插入位置
            subtree.right = self.insert_data(subtree.right, value)

        return subtree

    # 在二叉查找树中插入数据,该方法主要考虑是否插入，如果插入则去调用真正的插入方法
    def add(self, value):
        # 先查找数据 看 是否已经存在
        node = self.search(self.root, value)
        if node:            # node 存在说明在树中有该值，则不需要再插入
            return False
        else:
            self.root = self.insert_data(self.root, value)      # 执行真正的插入操作
            return True


if __name__ == '__main__':
    tree = Tree()
    # tree.init_data(node_list)

    tree.add(60)
    tree.add(50)
    tree.add(70)
    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
    tree.add(55)
    print(tree.root.left.right)

