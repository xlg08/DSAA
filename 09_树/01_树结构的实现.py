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

        # 遍历原数据列表 先封装成node 再将节点进行保存，放到一个容器中，放到一个字典中，字典的键为 node 的值
        for d in datas:
            node = Node(d['data'], d['left'], d['right'])       # 封装node节点
            node_dict[d['data']] = node         # 将节点保存到字典中

        # 使节点与节点之间产生关联
        for d in datas:
            node = node_dict[d['data']]         # 从字典中取出节点

            if node.left:       # 如果存在左子节点
                node.left = node_dict[node.left]        # 将子节点挂到父节点左边
            if node.right:      # 如果存在右子节点
                node.right = node_dict[node.right]      # 将子节点挂到父节点右边
            if d['is_root']:        # 如果是根节点，则将该节点赋给根
                self.root = node





if __name__ == '__main__':

    tree = Tree()
    tree.init_data(node_list)
