### 이진 탐색 트리의 검색

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역변수 선언 부분

memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인 코드 부분

node = TreeNode()   # 노드 생성
node.data = nameAry[0]
root = node     # 첫번째 노드를 루트 노드로 지정
memory.append(node) # 생성한 노드를 메모리에 저장

for name in nameAry[1:]:    # nameAry 두번째부터 모두 처리
    node = TreeNode()       # 새 노드 생성
    node.data = name        # 새 노드에 데이터 입력
    current = root          # 루트 노드를 현재 작업 노드로 지정
    while 1:
        if name < current.data:     # 입력할 값을 현재 작업 노드의 값과 비교
            if current.left == None:    # 현재 작업 노드의 왼쪽이 비었는지 확인
                current.left = node     # 새 노드를 현재 작업 노드의 왼쪽 링크에 연결
                break                   # 무한 반복 종료
            current = current.left      # 왼쪽 서브 트리를 현재 작업 노드로 변경하고 다시 진행
        else:   # 새 작업 노드가 더 클 경우
            if current.right == None:   # 현재 작업 노드의 오른쪽이 비어있는지 확인
                current.right = node    # 새 노드를 현재 작업 노드의 오른쪽 링크에 연결
                break                   # 무한 반복 종료
            current = current.right     # 오른쪽 서브 트리를 현재 작업 노드로 변경하고 다시 진행
    memory.append(node)

findName = input('찾을 그룹 이름 --> ')
current = root  # 루트 노드부터 검색 시작
while 1:
    if findName == current.data:    # 데이터를 찾으면 종료
        print(findName, '을(를) 찾음')
        break
    elif findName < current.data:   # 찾을 데이터가 더 작으면
        if current.left == None:    # 왼쪽 링크가 비어있다면 못찾은것으로 하고 종료
            print(findName, '이(가) 트리에 없음')
            break
        current = current.left      # 왼쪽 서브 트리를 현재 작업 노드로 변경하고 다시 진행
    else:       # 찾을 데이터가 더 큰 경우
        if current.right == None:   # 오른쪽 링크가 비어있다면 못찾은것으로 하고 종료
            print(findName, '이(가) 트리에 없음')
            break
        current = current.right     # 오른쪽 서브 트리를 현재 작업 노드로 변경하고 다시 진행
