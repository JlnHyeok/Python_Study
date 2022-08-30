'''
개념 : 각 원소마다 모든 값을 순회해야 할 떄, O(N^2)
      연속하다는 특성을 이용하여 처리, O(N)
      두개의 포인터(커서)가 움직이면서 계산
      처음부터 생각하기 어렵다, 쉬운 방법부터 생각하자.

1. 아이디어 : FOR문으로 각 숫자의 위치에서 이후 K개의 수를 더함
            이떄마다 최대값으로 갱신 -> 시간복잡도가 O(N X K)인데  N과 K 는 최대  100,000 이므로 2억을 초과한다.
            -> 투 포인터를 활용
            처음에 K개의 값을 구함
            FOR문 : 다음 인덱스의 값을 더하고, 앞의 값을 뺸다.
            이떄 , 최대값을 갱신

2. 시간 복잡도 : 숫자 개수만큼 FOR => O(2 X N) -> O(N)

3. 자료구조 : 전체 정수 배열 -> INT[]
            합한 수 -> INT
'''

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
nums = list(map(int,input().split()))
each = 0
# k개를 더해주자
for i in range(K):
    each += nums[i]
maxv = each

# 다음인덱스 더해주고 이전 인덱스 뺴주기
for i in range(K,N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv,each)

print(maxv)