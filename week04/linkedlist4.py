from ctypes.wintypes import tagMSG

class Node:
    def __init__(self, data, link= None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head: # 링크드리스트가 비어있는 상태이면
            self.head = Node(data) # 새 노드를 head에 연결
            return
        current = self.head
        while current.link:
            current = current.link # 다음 노드로 이동
        current.link = Node(data)

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return f"{target}을 찾았습니다."
            else:
                current = current.link
        return f"{target}을 찾지 못하였습니다."

    def remove(self, target):
        current = self.head
        if self.head.data == target:
            self.head = self.head.link
            current.link = None
            return
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link
                current.link = None
                return
            previous = current
            current = current.link

    def __str__(self):
        node = self.head
        result = ""
        while node is not None:
            if node.link is not None:
                result += str(node.data) + " -> "
            else:
                result += str(node.data)
            node = node.link
        return result

ll = LinkedList()
ll.append(1)
ll.append(5)
ll.append(8)
print(ll)
ll.remove(1)
ll.remove(5)
ll.remove(8)
ll.append(10)
ll.append(-9)
print(ll.search(-9))
print(ll)
ll.remove(-9)
print(ll)
print(ll.search(-9))




