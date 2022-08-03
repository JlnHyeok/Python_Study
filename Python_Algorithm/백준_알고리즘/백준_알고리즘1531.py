n,m=map(int,input().split())

x1 = [0 for _ in range(n)]
y1 = [0 for _ in range(n)]
x2 = [0 for _ in range(n)]
y2 = [0 for _ in range(n)]

for i in range(n):
    x1[i],y1[i],x2[i],y2[i]=map(int,input().split())


num_p_x = [0 for _ in range(101)]
num_p_y = [0 for _ in range(101)]
num_p_xy = [[0 for _ in range(101)] for _ in range(101)]


for i in range(n):
    for k in range(x1[i],x2[i]+1):
        for j in range(y1[i],y2[i]+1):
            num_p_xy[k][j]+=1

a = [0 for _ in range(101)]
for i in range(1,len(num_p_xy)):
    for j in range(m+1,101):
        a[j]+= num_p_xy[i].count(j)

print(sum(a))
