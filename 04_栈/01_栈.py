from collections import deque


class Stack:        # 栈
    def __init__(self):
        self.item = deque()

    def put(self, value):
        self.item.append(value)

    def pop(self):
        return self.item.pop()


if __name__ == '__main__':
    s = Stack()
    s.put("张三")
    s.put("李四")
    s.put("王五")
    s.put("赵六")

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
