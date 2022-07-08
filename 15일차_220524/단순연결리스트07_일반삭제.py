### 단순 연결 리스트 삭제 : 일반 버전

## 전역 변수 선언 부분

memory = []  # 생성한 노드를 넣는 메모리
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']


## 클래스와 함수 선언 부분

class Node:
    def __init__(self):
        self.data = None
        self.link = None


# 출력함수

def printNodes(start):
    current = start
    if current == None:  # 노드가 하나도 없는 경우 그냥 반환
        return
    print(current.data, end='->')  # 현재 노드를 출력

    while current.link != None:
        current = current.link
        print(current.data, end='->')
    print()

# 삭제 함수

def deleteNode(deleteData):
    global head, current, pre

    # 첫번째 노드를 삭제
    if head.data == deleteData:
        current = head  # 현재 노드를 헤드 노드와 동일하게 만든다.
        head = head.link    # 헤드 노드를 다음 노드로 변경
        del (current)       # 첫번째 노드를 삭제
        return

    # 첫번째 외 노드 삭제
    current = head
    while current.link != None:     # 현재 노드가 마지막이 아닐때까지 반복
        pre = current   # 현재 노드를 이전 노드로 지정
        current = current.link  # 현재 노드를 한 칸 이동
        if current.data == deleteData:  # 현재 노드의 데이터가 삭제할 데이터라면
            pre.link = current.link     # 이전 노드의 링크를 현재 노드로 변경
            del(current)    # 현재 노드 삭제
            return




# 메인 코드 부분

if __name__ == '__main__':
    node = Node()  # 첫번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node  # 현재 노드를 이전 노드로 저장하고
        node = Node()  # 새 노드를 생성
        node.data = data  # 노드에 데이터를 넣고
        pre.link = node  # 이전 노드의 링크에 새 노드를 대입
        memory.append(node)  # 새 노드를 메모리에 넣는다.

    printNodes(head)  # 생성이 완료된 단순연결리스트를 출력

deleteNode('다현')
printNodes(head)

deleteNode('쯔위')
printNodes(head)

deleteNode('지효')
printNodes(head)

deleteNode('재남')    # 존재하지 않는 노드 : 아무 변화도 일어나지 않는다.
printNodes(head)