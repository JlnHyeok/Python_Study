n = int(input())
k = int(input())
cnt = 0

for i in range(1,n+1):
    c = i

    for j in range(2,k+1):
        while c%j==0:
            c=c//j
    if c==1:
        cnt+=1

print(cnt)