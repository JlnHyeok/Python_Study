'''
개념 : 모든 경우의 수를 확인해야 할 때
        - for로는  확인이 불가능할 경우 (깊이가 달라질떄)
            ex) 이중 for , 3중 for ..등등 계속 바뀔떄
백준 15649

1. 아이디어
    - 1부터 N중에 하나를 선택
    - 다음 1부터 선택할 때 이미 선택한 값이 아닌경우 선택
    - 재귀 함수에서 M개를 선택할 경우 프린트

2. 시간복잡도
    - 중복이 가능한 경우 : N^N , N은 8까지 가능 < 2억
    - 중복이 불가한 경우 : N! , N은 10까지 가능 < 2억
    - N이 작다.
3. 자료구조
    - 방문 여부 확인 배열 : bool[]
    - 선택한 값 입력 배열 : int[]
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs = []
chk = [False for _ in range(N+1)] # 배열 인덱스와 통일시켜주려고

def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(1,N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()    # 마지막 값을 뺴주고 재귀해야 리스트에 값이 2개가 들어가진다.
recur(0)