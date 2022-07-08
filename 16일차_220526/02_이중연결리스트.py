### 이중연결리스트 구현

## 전역 변수 선언 부분

memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']

## 클래스와 함수 선언 부분

class Node2:
    def __init__(self):
        self.plink = None   # 앞쪽 링크
        self.data = None
        self.nlink = None   # 뒷쪽 링크

# 출력함수

def printNodes(start):
    current = start
    if current.nlink == None:
        return
    # 시작 노드부터 마지막 노드까지 출력
    print('정방향 -->',end = ' ')
    print(current.data, end= '->')
    while current.nlink != None:    # 현재 노드의 뒷쪽 링크가 None이 될 때까지 반복
        current = current.nlink
        print(current.data, end = '->')
    print()

    # 반대로 마지막 노드부터 시작 노드까지 출력

    print('역방향 --->', end = ' ')
    print(current.data, end = '->')
    while current.plink != None:    # 현재 노드의 앞쪽 링크가 None이 될 때까지 반복
        current = current.plink
        print(current.data, end = '->')


## 메인코드 부분

if __name__ == '__main__':
    node = Node2()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node2()  # 새 노드 생성
        node.data = data
        pre.nlink = node
        node.plink = pre    # 두 노드를 상호 링크로 연결
        memory.append(node)

    printNodes(head)