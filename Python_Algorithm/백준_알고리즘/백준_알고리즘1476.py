e,s,m = map(int,input().split())

if e == 15:
    e = 0
if s == 28:
    s = 0
if m == 19:
    m = 0


i = 1
while 1:
    a = i%15
    b = i%28
    c = i%19
    if a==e and s==b and c==m:
        break
    i += 1
print(i)