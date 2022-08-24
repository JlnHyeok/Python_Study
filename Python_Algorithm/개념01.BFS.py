'''
BFS : 너비우선탐색
자식들을 먼저 탐색하고 그 다음 순차적으로 자손노드 탐색

1. 아이디어
- 2중 for => 값 1 && 방문 x => BFS
- BFS 돌면서 그림 개수 +1, 최대값 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : 500 x 500 (최대) -> 점의 개수
- E : V X 4 (넉넉잡아서) = 4 * 500 * 500 -> 선의 개수
- V+E = 약 100만 < (1초연산)2억 ==> 가능

3. 자료구조
- 그래프 전체 지도 int[][]
- 방문 : bool[][]
- Queue(BFS)
'''
# 입출력 속도를 빠르게 해주는 코드 (습관화 하자)
import sys
input = sys.stdin.readline
# n : y축 // m : x 축
n,m=map(int,input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]

dy=[0,1,0,-1]
dx=[1,0,-1,0]
# (1,0) 오른쪽 , (0,1) 아래쪽 , (-1,0) 왼쪽 , (0,-1) 위쪽 방향

def bfs(y,x):
    rs = 1 # (초기 크기 = 1)
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):  # 4방향에 대해    
            ny = ey + dy[k] # y,x축 각각 이동해서 확인
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m: # 사이즈를 넘어가지 않는 범위에서
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs+=1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt=0
maxv = 0

for j in range(n):  # 2중for문은 y축부터 돌도록 하자
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 갯수 +1
            cnt+=1
            # BFS 를 통해 그림의 크기를 구해주고
            # 최대값 갱신
            maxv = max(maxv,bfs(j,i))
            
print(cnt)
print(maxv)