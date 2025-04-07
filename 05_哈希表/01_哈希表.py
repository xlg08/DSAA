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


    def put(self, key, value):      # 存放数据

        s = Slot(key, value)
        index = self.__get_index(key)
        if self.items[index] == None:
            self.items[index] = s


    def get(self, key):     # 获取数据
        index = self.__get_index(key)         # 获取key对应的索引值
        return self.items[index]


if __name__ == '__main__':

    hashTable = HashTable()
    hashTable.put("张三", "是个好人")
    print(hashTable.get("张三"))



