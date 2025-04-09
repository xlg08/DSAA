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
    def __init__(self, root=None):
        self.root = root

    def init_data(self, datas):

        node_dict = {}

        # 遍历原数据列表 先封装成node 再将节点进行保存，放到一个容器中，放到一个字典中，字典的键为 node 的值
        for d in datas:
            node = Node(d['data'], d['left'], d['right'])  # 封装node节点
            node_dict[d['data']] = node  # 将节点保存到字典中

        # 使节点与节点之间产生关联
        for d in datas:
            node = node_dict[d['data']]  # 从字典中取出节点

            if node.left:  # 如果存在左子节点
                node.left = node_dict[node.left]  # 将子节点挂到父节点左边
            if node.right:  # 如果存在右子节点
                node.right = node_dict[node.right]  # 将子节点挂到父节点右边
            if d['is_root']:  # 如果是根节点，则将该节点赋给根
                self.root = node

    # 深度优先 先序遍历
    def iter_node1(self, node):
        if node:      # 当还存在节点时执行
            # print(node)     # 打印当前节点
            print(node.data, end='\t')      # 打印当前节点的值
            self.iter_node1(node.left)      # 将该节点的左节点再作为根调用函数
            self.iter_node1(node.right)     # 将该节点的右节点再作为根调用函数
            # print()


    # 广度优先
    def iter_node2(self, node):

        node_list = [node]      # 先传入的根节点，会先将根节点放入到列表中
        for n in node_list:     # 遍历列表中的节点，以及在循环中添加到列表中的节点
            print(n.data)       # 输出当前节点的值
            if n.left:    # 当存在左子节点时，将子节点添加到列表中
                node_list.append(n.left)
            if n.right:     # 当存在右子节点时，将子节点添加到列表中
                node_list.append(n.right)


    def reverse(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.reverse(node.left)
            self.reverse(node.right)



if __name__ == '__main__':
    tree = Tree()
    tree.init_data(node_list)
    # tree.iter_node1(tree.root)
    # tree.iter_node2(tree.root)
    tree.reverse(tree.root)
    tree.iter_node2(tree.root)