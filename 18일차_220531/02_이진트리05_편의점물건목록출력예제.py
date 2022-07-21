### 이진 탐색 트리 응용 : 편의점에서 판매된 물건 목록 출력하기

import random

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역 변수 선언 부분
memory = []
root = None

# 편의점에서 파는 물건 종류를 7개로 정한다
dataAry = ['바나나맛우유','레쓰비캔커피','츄파춥스','도시락','삼다수','코카콜라','삼각김밥']
sellAry = [random.choice(dataAry) for _ in range(20)]    # 랜덤하게 20개를 중복해서 판매한다.
print('오늘 판매된 물건(중복 O) --> ', sellAry)  # 중복해서 판매한 물품을 출력한다.

## 메인 코드 부분
node = TreeNode()
node.data = sellAry[0]
root = node
memory.append(node)

for name in sellAry[1:]:
    node = TreeNode()
    node.data = name
    current = root
    while 1:
        if name == current.data:    # 이미 판매한 물품일 경우 아무 작업도 하지 않고 넘어간다.
            break                   # 중복된 물품을 제거하는 코드
        if name < current.data:
            if current.left == None:
                current.left = node
                memory.append(node)
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                memory.append(node)
                break
            current = current.right
print('이진 탐색 트리 구성 완료')

# 전위 순회 방식으로 이진 탐색 트리 출력
def preorder(node):
    if node == None:
        return
    print(node.data, end = ' ')
    preorder(node.left)
    preorder(node.right)

print('오늘 판매된 물건(중복 X) --> ', end = ' ')
preorder(root)