'''
1. 아이디어
- 2중 for => 값 1 && 방문 x => BFS
- BFS 돌면서 그림 개수 +1, 최대값 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : 500 x 500 (최대)
- E : V X 4 (넉넉잡아서) = 4 * 500 * 500
- V+E = 약 100만 < 2억 ==> 가능

3. 자료구조
- 그래프 전체 지도 int[][]
- 방문 : bool[][]
- Queue(BFS)
'''
# 입출력 속도를 빠르게 해주는 코드 (습관화 하자)
# import sys
# input = sys.stdin.readline
# # n : y축 // m : x 축
# n,m=map(int,input().split())
# map = [list(map(int, input().split())) for _ in range(n)]

dic = {1 : '가', 2 : '나', 3 : '다'}

for i in dic:
    print(dic[i])