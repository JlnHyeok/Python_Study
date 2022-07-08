### 이진 트리의 순회(재귀 함수 사용)

## 이진 트리 노드 생성

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = TreeNode()  # 루트 노드 생성
node1.data = '화사'

node2 = TreeNode()  # 루트 노드의 왼쪽 자식 노드
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()  # 루트 노드의 오른쪽 자식 노드
node3.data = '문별'
node1.right = node3

node4 = TreeNode()  # 노드2의 왼쪽 자식 노드
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()  # 노드2의 오른쪽 자식 노드
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()  # 노드3의 왼쪽 자식 노드
node6.data = '선미'
node3.left = node6

## 전위 순회를 위한 재귀 함수

def preorder(node):
    if node == None:    # 노드가 없다면 함수를 종료
        return
    print(node.data, end = '->')    # 루트 -> 왼쪽 -> 오른쪽
    preorder(node.left)
    preorder(node.right)

## 중위 순회를 위한 재귀 함수

def inorder(node):
    if node == None:
        return
    inorder(node.left)  # 왼쪽 -> 루트 -> 오른쪽
    print(node.data, end = '->')
    inorder(node.right)

## 후위 순회를 위한 재귀 함수

def postorder(node):
    if node == None:
        return
    postorder(node.left)    # 왼쪽 -> 오른쪽 -> 루트
    postorder(node.right)
    print(node.data, end  = '->')

print('전위 순회 :', end = ' ')
preorder(node1)
print('끝')

print('중위 순회 :', end = ' ')
inorder(node1)
print('끝')

print('후위 순회 :', end = ' ')
postorder(node1)
print('끝')