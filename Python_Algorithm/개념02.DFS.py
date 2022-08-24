'''
DFS = 깊이우선탐색
자식의 자식을 먼저 탐색
stack 과 재귀함수로 풀 수 있다.

1. 아이디어
- 2중 for , 값 1 && 방문 X -> DFS
- DFS를 통해 찾은 값을 저장 후 정렬해서 출력

2. 시간복잡도
- DFS : O(V+E)
- V,E : N^2, 4N^2
- V+E : 5N^2 ~= N^2 ~= 625 (2억보다 작다) -> 가능

3. 자료구조
- 그래프 저장 : int[][]
- 방문 여부 : bool[][]
- 결과값 : int[]

'''

import sys
input = sys.stdin.readline  # 엔터친게 특수문자로 들어오게 된다.

n = int(input())
# input().strip()를 해준다.
map = [list(map(int,input().strip())) for _ in range(n)]
chk = [[False for _ in range(n)] for _ in range(n)]

result = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each +=1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny,nx)  # 재귀 호출

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문 체크 표시
            chk[j][i] == True
            # DFS로 크기 구하기
            each = 0
            dfs(j,i)
            result.append(each)
            # 크기를 결과 리스트에 넣기

result.sort()
print(len(result))
for i in result:
    print(i)