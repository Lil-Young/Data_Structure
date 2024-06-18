# 연결 리스트 중간에 데이터 넣기

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
node1 = Node(1)
head = node1

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

for index in range(2, 10):
    add(index)

node = head
while node.next:
    print(node.data, '->', end=' ')
    node = node.next
print(node.data) # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

# 중간 삽입
node3 = Node(1.5)
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next
node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data, '->', end=' ')
    node = node.next
print(node.data) # 1 -> 1.5 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
