from collections import deque


class DoubleQueue:  # 双端队列
    def __init__(self):
        self.item = deque()

    def put(self, value):
        self.item.append(value)

    def put2(self, value):
        self.item.appendleft(value)

    def pop(self):
        return self.item.pop()

    def pop2(self):     # 头进头出
        return self.item.popleft()


if __name__ == '__main__':
    db = DoubleQueue()
    db.put("张三")
    db.put("李四")
    db.put("王五")
    db.put("赵六")

    print(db.pop2())
    print(db.pop2())
    print(db.pop2())
    print(db.pop2())