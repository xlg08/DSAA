"""
    使用链表的方法解决hash冲突

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
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

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

        s = Slot(key, value)    # 封装slot节点
        index = self.__get_index(key)   # 获取默认的索引位置
        # 情况一：索引位置是空的
        if self.items[index] == None:
            self.items[index] = s       # 直接赋值
        # 情况二：索引位置是非空的
        else:
            # 问题一：所占空间的数据的key 与 传入数据 key 相同
            if self.items[index].key == key:
                self.items[index].value = value
            # 问题二：所占空间的数据的key 与 传入数据 key 不相同
            else:
                temp = self.items[index]        # 记录当前节点
                temp_next = self.items[index].next      # 记录下一个节点
                while temp_next is not None:
                    if temp_next.key == key:
                        temp_next.value = value     # 更新原来节点的数据
                        return
                    temp = temp_next
                    temp_next = temp.next
                temp.next = s

    def get(self, key):     # 获取数据
        index = self.__get_index(key)         # 获取key对应的索引值

        if self.items[index]:
            if self.items[index].key == key:
                return self.items[index].value
            else:
                temp_next = self.items[index].next
                while temp_next is not None:
                    if temp_next.key == key:
                        return temp_next.value
                    temp_next = temp_next.next
                return None
        return None

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



