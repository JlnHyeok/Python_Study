### 개선된 무방향 그래프 ###

## 클래스 선언 부분 ##
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 전역 변수 선언 부분 ##
G1 = None
nameAry = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0, 1, 2, 3, 4, 5

## 행과 열의 주석을 추가해서 출력하는 함수 ##
def printGraph(g):
    print('  ', end=' ')
    for v in range(g.SIZE):
        print(nameAry[v], end=' ')  # 제목 출력
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end=' ')  # 제목 출력
        for col in range(g.SIZE):
            print(g.graph[row][col], end='   ')  # 인접행렬 출력
        print()
    print()

## 메인 코드 부분 ##
gSize = 6  # 정점 개수를 6개로 지정
G1 = Graph(gSize)  # 그래프 생성
# 그래프의 간선 연결
G1.graph[문별][솔라] = 1; G1.graph[문별][휘인] = 1
G1.graph[솔라][문별] = 1; G1.graph[솔라][쯔위] = 1
G1.graph[휘인][문별] = 1; G1.graph[휘인][쯔위] = 1
G1.graph[쯔위][솔라] = 1; G1.graph[쯔위][휘인] = 1; G1.graph[쯔위][선미] = 1; G1.graph[쯔위][화사] = 1
G1.graph[선미][쯔위] = 1; G1.graph[선미][화사] = 1
G1.graph[화사][쯔위] = 1; G1.graph[화사][선미] = 1

print('** G1 무방향 그래프 **')
printGraph(G1)  # 인접행렬 출력






