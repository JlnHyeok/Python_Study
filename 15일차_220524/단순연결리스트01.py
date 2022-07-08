# 데이터가 5개인 단순연결리스트 생성

## 노드 클래스 정의

class Node:
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()  # 노드1 객체 생성
node1.data = '다현'

node2 = Node()
node2.data = '정연'

node1.link = node2  # 노드1과 노드2를 연결

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
print(node1.link.link.link.link.data, end=' ')
