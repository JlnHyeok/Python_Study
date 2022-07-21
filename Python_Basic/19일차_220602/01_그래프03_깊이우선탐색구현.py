### 깊이 우선 탐색의 구현 ###

## 클래스 선언 부분 ##
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 전역 변수 선언 부분 ##
G1 = None
stack = []
visitedAry = []  # 방문한 정점

## 메인 코드 부분 ##
G1 = Graph(4)
G1.graph[0][2] = 1; G1.graph[0][3] = 1  # 정점 A 출발
G1.graph[1][2] = 1   # 정점 B 출발
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1  # 정점 C 출발
G1.graph[3][0] = 1; G1.graph[3][2] = 1  # 정점 D 출발

print('** G1 무방향 그래프 **')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end=' ')
    print()

current = 0   # 시작 정점(첫번째 정점 A 방문)
stack.append(current)   # 스택에 A를 넣고
visitedAry.append(current)  # 방문기록에도 A를 넣는다.

# 스택에 아무것도 없을 때까지 반복 (스택이 비었다는 것은 모든 정점을 방문했다는 의미)
while len(stack) != 0:
    next = None  # 다음에 방문할 정점을 None으로 초기화
    for vertex in range(4):
        if G1.graph[current][vertex] == 1:  # 현재 정점과 연결된 다른 정점을 찾는다.
            if vertex in visitedAry:  # 방문한 적이 있는 정점이면 탈락
                pass
            else:   # 방문한 적이 없으면 다음 정점으로 지정
                next = vertex
                break
    if next != None:  # 다음에 방문할 정점이 있는 경우(다음 정점을 찾았다면)
        current = next  # 다음 정점을 현재 정점으로 지정
        stack.append(current)  # 스택에 넣는다.
        visitedAry.append(current)  # 방문 배열에도 넣는다.
    else: # 다음에 방문할 정점이 없는 경우(다음 정점을 찾지 못했다면)
        current = stack.pop()  # 스택에서 정점을 꺼내서 현재 정점으로 지정한다.

print('방문 순서 -->', end=' ')
for i in visitedAry:  # 방문한 순서대로 정점을 출력한다.
    print(chr(ord('A')+i), end=' ')  # 문자 A를 유니코드로 변경한 후 다신 문자로 변환해서 출력
















