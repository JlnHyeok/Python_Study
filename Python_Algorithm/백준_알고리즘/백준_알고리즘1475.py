import math
n = input()
k=[0 for _ in range(10)]
for i,v in enumerate('0123456789'):
    k[i] = n.count(v)
k[6] = math.ceil((k[6]+k[9])/2)
k[9] = k[6]
ans = max(k)
print(ans)
