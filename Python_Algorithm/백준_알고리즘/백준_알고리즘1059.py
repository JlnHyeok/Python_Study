
L = int(input())
arr_L = list(map(int,input().split()))
n = int(input())
arr_L = sorted(arr_L)

A = 0
B = 0
cnt=0
for i in arr_L:
    if n>=i:
        A=i
    elif n<=i:
        B=i
        break
if A==n or B==n:
    print(0)
    exit()

A+=1
B-=1
n1 = n-A
n2 = B-n
n3 = (n1)*(n2)
print(n1+n2+n3)