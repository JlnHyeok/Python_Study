### 데이터가 5개인 단순연결리스트 삽입(개선버전)

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

newNode = Node()    # 새 노드 생성
newNode.data = '재남'     # 데이터에 재남을 대입
newNode.link = node2.link   # 정연의 링크를 복사
node2.link = newNode        # 정연 노드의 링크에 새 노드를 지정


current = node1     # 첫번째 노드를 현재노드로 지정
print(current.data, end='->')
while current.link != None:     # 현재노드의 링크가 비어있지 않은 동안 반복
    current = current.link      # 다음노드를 현재노드로 지정
    print(current.data, end='->')
