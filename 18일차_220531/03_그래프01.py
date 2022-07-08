### 무관한 그래프와 방향 그래프의 구현

## 클래스 선언 부분
class Graph:
    def __init__(self, size):
        self.SIZE = size    # 생성될 그래프의 크기(그래프의 정점 개수)
        self.graph =[[0 for _ in range(size)] for _ in range(size)]     # 0으로 초기화된 2차원배열

## 전역 변수 선언 부분
G1, G3 = None, None

## 메인 코드 부분
G1 = Graph(4)   # 무방향 그래프로 사용할 G1 그래프 생성(간선없이 정점만 4개)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1  # 정점 A에서 출발
G1.graph[1][0] = 1; G1.graph[1][2] = 1  # 정점 B에서 출발
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1  # 정점 C에서 출발
G1.graph[3][0] = 1; G1.graph[3][2] = 1  # 정점 D에서 출발

print('--G1 무방향 그래프--')
for row in range(4):   #4 x 4 인접행렬 출력
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()

G3 = Graph(4)   # 방향 그래프로 사용할 G3 그래프 생성(간선없이 정점만 4개)
G3.graph[0][1] = 2; G3.graph[0][2] = 1  # 정점 A에서 출발
G3.graph[3][0] = 1; G3.graph[3][2] = 1  # 정점 D에서 출발

print('--G3 방향 그래프--')
for row in range(4):
    for col in range(4):
        print(G3.graph[row][col], end = ' ')
    print()