import math
T = int(input())

for i in range(T):
    N,M = map(int,input().split())

    ans=math.factorial(M)
    div = math.factorial(N)*math.factorial(M-N)

    print(int(ans/div))

