import math

a = str(math.factorial(int(input())))
cnt = 0
for i in range(len(a)-1,0,-1):
    if a[i]!='0':
        break
    cnt+=1

print(cnt)
