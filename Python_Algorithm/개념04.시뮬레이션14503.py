'''
개념 : 각 조건에 맞는 상황을 구현하는 문제
        - 지도상에서 이동하면서 탐험하는 문제
        - 배열 안에서 이동하면서 탐험하는 문제
    : 별도의 알고리즘 없이 풀수있으나, 구현력 중요
    : 매 시험마다 1문제 이상 무조건 출제

1. 아이디어 : 특정 조건 만족하는 한 계속 이동 -> while
             4방향 탐색 먼저 수행 -> 빈칸 있을 경우 이동
             4방향 탐색 안될 경우, 뒤로 한칸 가서 반복

2. 시간 복잡도 : while문 최대 : N X N -> 50 X 50 = 2500 < 2억
               각 칸에서 4방향 연산 수행
               -> O(N X N)

3. 자료구조 : 전체 지도 -> int[][]
             내 위치, 방향 -> int, int, int
'''

import sys
input = sys.stdin.readline

N,M = map(int, input().split())

y,x,d = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

dy = [-1,0,1,0]
dx = [0,1,0,-1]


while 1 :
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1
    sw = False
    for i in range(1,5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 0:
                # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
                d = (d-i+4)%4
                y = ny
                x = nx
                sw = True
                break

    # 4방향 모두 있지 않은 경우
    if sw == False:
        # 바라보는 방향을 유지한 채로 한칸 후진
        # 후진 방향이 막혀있는지 확인
        ny = y - dy[d]
        nx = x - dx[d]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 1:
                break
            else:   # 여기선 청소 하면 안된다.
                y = ny
                x = nx
        else:
            break
print(cnt)