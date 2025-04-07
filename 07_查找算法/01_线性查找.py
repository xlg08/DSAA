# 方法一
def line_search1(find_value, args):
    for index, value in enumerate(args):
        if find_value == value:
            return index
    return -1


# 方法二
def line_search2(fun, args):
    for index, value in enumerate(args):
        if fun(value):
            return index
    return -1


# 方法三
def line_search3(find_value, args):
    if len(args) == 0:      # 如果最后传入空列表，则返回最后遍历完列表中没有
        return -1
    index = len(args) - 1       # 从最后一个元素向前到，向前遍历
    if args[index] == find_value:
        return index
    return line_search3(find_value, args[:index])   # 去掉每次的最后一个元素，再调用函数


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # print(line_search1(5, nums))

    # print(line_search2(lambda x: x == 5, nums))

    print(line_search3(5, nums))
