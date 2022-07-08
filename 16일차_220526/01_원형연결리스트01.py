### 원형 연결 리스트 생성

## 전역 변수 선언 부분

memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']

## 클래스와 함수 선언 부분

class Node:
    def __init__(self):
        self.data = None
        self.link = None

# 출력 함수

def printNodes(start):
    current = start # 전달받은 시작 노드를 현재 노드로 지정
    if current.link == None:    # 노드에 데이터가 하나도 없는 연결리스트인 경우 그냥 반환
        return
    print(current.data, end = '->')     # 현재 노드 출력
    while current.link != start:        # 현재 노드의 링크가 첫번째 노드가 아닐때까지 반복
        current = current.link          # 전체 노드를 한바퀴 방문한다.
        # 현재 노드의 링크가 첫번째 노드라면 원형연결리스트에서는 마지막 노드를 의미한다
        print(current.data, end = '->')
    print()

## 메인 코드 부분

if __name__ == '__main__':
    node = Node()   # 새 노드 생성
    node.data = dataArray[0]    # 첫번째 노드
    head = node
    node.link = head            # 노드의 링크를 헤드에 연결(첫번째 노드이므로 자신이 자신과 연결된 상태)
    memory.append(node)

    for data in dataArray[1:]:  # 두번째 노드 이후
        pre = node  # 현재 노드를 이전 노드로 지정
        node = Node()   # 새 노드 생성
        node.data = data    # 노드에 데이터 넣고
        pre.link = node     # 이전 노드의 링크에 새 노드 연결
        node.link = head    # 추가한 노드의 링크를 헤드와 연결해서 원형연결리스트 구조를 유지
        memory.append(node) # 새 노드를 메모리에 넣는다.

    printNodes(head)        # 생성된 원형연결리스트를 출력
