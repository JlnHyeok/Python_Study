### 높이가 2인 완전 이진 트리의 생성

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

print(node1.data)
print(node1.left.data, node1.right.data)
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)