class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

s1 = Stack()
s2 = Stack()

print(s1.isEmpty())
print(s2.isEmpty())
s1.push("자료구조")
print(s1.isEmpty())
print(s2.isEmpty())
s1.push("데이터베이스")
print(s1.size())
print(s1.peek())