import math
def toF(x):
    a = float(str(x)[0:5])
    return a

n = int(input())
nl = [None for _ in range(n)]
for i in range(n):
    nl[i] = float(input())


p = 1

while 1:
    cnt = 0
    for i in nl:
        if toF(math.ceil(i*p) / p) == i or toF(math.floor(i*p) / p) == i :
            cnt+=1
        if cnt == n:
            print(p)
            exit()
    p+=1




# 소수점 고정시킬떄
# a = '0.22255'
# print(float(a[:5]))