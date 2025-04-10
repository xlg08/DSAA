'''
    BST 二叉查找树
        其每个节点的左子节点小于该节点，每个节点的右子节点小于该节点。

'''

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

    # 在二叉查找树上查找某个值
    # subtree 为分支，
    #       首次传入根节点，即：从整棵树上查找
    #       通过比较后，传入左或右子节点，即：从左或右分支上进行查找
    #       依次递归
    def search(self, subtree, value):
        if subtree is None:     # 如果传入的当前分支(包括根)是空，则没有对应的值，返回空
            return None
        elif subtree.data > value:      # 如果传入的值比当前结点的值小，则再从左子树上去查找
            return self.search(subtree.left, value)
        elif subtree.data < value:      # 如果传入的值比当前结点的值大，则再从右子树上去查找
            return self.search(subtree.right, value)
        else:       # 如果传入的值与当前结点的值相等，则返回当前节点
            return subtree


if __name__ == '__main__':
    tree = Tree()
    tree.init_data(node_list)

    print(tree.search(tree.root, 66))
    # print(tree.search(tree.root, 41).data)
