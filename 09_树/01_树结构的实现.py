'''
    @User: LG
    @Auther: http://www.xlonggang.cn
    @Date: 2025/4/7 0007 17:33 
    @Description: 
    @Project ：数据结构 
    @File    ：01_树结构的实现.py
    @version: 1.0
'''


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

class Node:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

class Tree:
    def __init__(self, root = None):
        self.root = root

    def init_data(self, datas):

        node_dict = {}

        # 遍历原数据列表 先封装成node 在
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

if __name__ == '__main__':
    tree = Tree()
    tree.init_data(node_list)
