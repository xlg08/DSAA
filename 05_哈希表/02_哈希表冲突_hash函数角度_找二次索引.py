"""
    使用二次探查的方法解决hash冲突

"""

class Array:
    def __init__(self, size=4):
        self.__size = size      # 记录容器的大小
        self.__item = [None] * size  # 分配空间
        self.__length = 0

    # 向数组中添加元素
    def __setitem__(self, key, value):
        self.__item[key] = value
        self.__length += 1

    # 从数组中获得元素
    def __getitem__(self, key):
        return self.__item[key]

    # 返回数组的大小
    def __len__(self):
        return self.__length

    def __iter__(self):
        for value in self.__item:
            yield value

class Slot():       # key value 结构作为节点  槽
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return f"key: {self.key},  value: {self.value}"

class HashTable():

    def __init__(self):
        self.size = 4
        self.items = Array(self.size)

    # 该方法使得所有类型都可以对数组长度取余,作为元素在数组中的索引
    def __get_index(self, key):
        # hash()是python中内置的方法，可以对对象进行hash操作，返回int类型
        return hash(key) % self.size

    # 该方法用于为put方法判断该元素最后应该存储在什么位置
    def __find_index_to_insert(self, key):
        index = self.__get_index(key)       # 获取 key 对应的索引，默认应该存储的位置
        if self.items[index] == None:       # 该判断本质上可以省略
            return index
        else:
            while self.items[index] is not None:
                if self.items[index].key == key:        # 获取到相同的 key
                    return index
                else:
                    index = (5 * index + 1) % self.size     # 在CPython中推荐的写新的索引值的写法
            return index

    def put(self, key, value):      # 存放数据

        s = Slot(key, value)
        # index = self.__get_index(key)     # 会发生哈希冲突的获取索引值的方法
        index = self.__find_index_to_insert(key)
        if self.items[index] == None:
            self.items[index] = s

    # 该方法用于get方法找到一个正确的索引
    def __find_key(self, key):
        index = self.__get_index(key)       # 默认情况下
        if self.items[index] == None:
            return None
        else:
            while self.items is not None:
                if key == self.items[index].key:        # 判断查找的key是否与item里的key相同
                    return index
                else:
                    index = (5 * index + 1) % self.size
            return None

    def get(self, key):     # 获取数据
        # index = self.__get_index(key)         # 获取key对应的索引值
        index = self.__find_key(key)       # 获取解决hash冲突的正确的索引
        return self.items[index]


if __name__ == '__main__':

    hashTable = HashTable()
    hashTable.put("name", "张三")
    hashTable.put("sex1", "男")
    hashTable.put("sex2", "女")
    hashTable.put("sex3", "不详")



    print(hashTable.get("name"))
    print(hashTable.get("sex1"))
    print(hashTable.get("sex2"))
    print(hashTable.get("sex3"))



