import sys

input = sys.stdin.readline

n = int(input())
x = [0 for _ in range(4)]
y = [0 for _ in range(4)]
for j in range(n):
    dx = []
    for i in range(4):
        x[i],y[i] = map(int,input().split())

    for i in range(3):
        for k in range(i+1,4):
            d = ((x[i] - x[k])**2 + (y[i] - y[k])**2)**0.5
            dx.append(d)
    dx = (set(dx))

    if len(dx) == 2:
        print(1)
    else:
        print(0)