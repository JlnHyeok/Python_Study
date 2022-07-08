### 단순 연결 리스트 삽입 : 일반 버전

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

# 삽입함수

def insertNode(findData, insertData):   # findData위치에 insertData 삽입
    global head, current, pre

    # 첫번째 노드 삽입
    if head.data == findData:
        node = Node()       # 새 노드 생성
        node.data = insertData
        node.link = head    # 링크를 헤드가 가리키는 노드(첫번째 노드)로 지정
        head = node         # 헤드를 새 노드로 변경
        return              # 함수를 종료

    # 중간에 노드 삽입
    current = head  # 현재 노드에 헤드를 저장
    while current.link != None:     # 현재 노드가 마지막이 아닐때까지 반복
        pre = current   # 현재 노드를 이전 노드로 지정
        current = current.link  # 현재 노드를 한 칸 이동(다음노드로)
        if current.data == findData:    # 현재 노드의 데이터가 찾을 데이터라면
            node = Node()   # 새 노드 생성
            node.data = insertData
            node.link = current     # 이전 노드와 현재 노드 사이에 새 노드 삽입
            pre.link = node
            return

    # 마지막 노드 삽입(찾을 데이터가 메모리에 없다면)
    node = Node()   # 새 노드 생성
    node.data = insertData
    current.link = node     # 현재 노드(마지막 노드)의 링크를 새 노드로 지정
                            # 새 노드가 마지막 노드가 된다.




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

    insertNode('다현','화사')   # 다현 노드 앞에 화사 노드 삽입 후 출력
    printNodes(head)

    insertNode('사나','솔라')
    printNodes(head)

    insertNode('재남','문별')
    printNodes(head)