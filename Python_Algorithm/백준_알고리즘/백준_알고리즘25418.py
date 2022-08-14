n1,n2 = map(int,input().split())
cnt = 0

def A():
    global cnt
    global n2
    if n2%2 == 1:
        n2 -=1
        cnt+=1
    else:
        if n2>=n1*2:
            n2/=2
            cnt+=1
        else:
            n2-=1
            cnt+=1

while n1!=n2:
    A()
print(cnt)