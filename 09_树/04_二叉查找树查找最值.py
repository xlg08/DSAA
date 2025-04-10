
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


    # 获取最小值
    def get_min(self, subtree):         # 先传入根节点
        if subtree is None:
            return None
        elif subtree.left is None:      # 根据二叉查找树的性质，如果没有左子节点了，则小值找到最后了
            return subtree
        else:
            # 根据二叉查找树的性质，最小值只需要在左子树上寻找
            return self.get_min(subtree.left)

    # 获取最大值
    def get_max(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self.get_max(subtree.right)

if __name__ == '__main__':
    tree = Tree()
    tree.init_data(node_list)

    print("该树的最小值是：", tree.get_min(tree.root))
    print("该树的最大值是：", tree.get_max(tree.root))