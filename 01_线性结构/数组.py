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

    # 迭代数据
    # yield 关键字 类似于 return ，只不过他返回一个生成器
    #       生成器（generator）的一部分（带yield的函数才是真正的迭代器）
    # 带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，
    #   next就相当于“下一步”生成哪个数，这一次的next开始的地方是接着上一次的next停止的地方执行的，
    #   所以调用next的时候，生成器并不会从函数定义的开始执行，只是接着上一步停止的地方开始，
    #   然后遇到yield后，return出要生成的数，此步就结束。

    def __iter__(self):
        for value in self.__item:
            yield value

if __name__ == '__main__':
    a1 = Array(4)
    print(a1._Array__item)
    # a1[0] = "哈哈"
    # a1[1] = "拉拉"
    #
    # print(a1[0])
    # print(a1[1])
    # print("-"*30)
    #
    # for i in a1:
    #     print(i)
    #
    # print(len(a1))
    # print(a1.__sizeof__())
    # print(id(a1))
    #
    # a2 = Array(4)
    # print(a2.__sizeof__())
    # print(id(a2))

