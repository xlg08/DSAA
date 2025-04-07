"""
    递归：
        条件：
            基线条件：循环体，主要递归执行的内容是什么
            递归条件：达到什么条件去调用他

    递归存在一个进栈问题，在递归次数太多时，不建议使用递归，因为可能会产生一个栈溢出的问题
"""


def count_down(i):
    print(i)
    if i <= 1:
        return
    else:
        count_down(i - 1)


if __name__ == '__main__':
    count_down(5)