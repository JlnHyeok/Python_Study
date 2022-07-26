x1,y1,x2,y2,x3,y3 = map(int,input().split())

d=[0 for _ in range(4)]

d1=(float)((x1-x2)**2+(y1-y2)**2)**0.5

d2=(float)((x1-x3)**2 + (y1-y3)**2)**0.5

d3=(float)((x2-x3)**2 + (y2-y3)**2)**0.5

l1=d1+d2
l2=d1+d3
l3=d2+d3

if x1==x2==x3 or y1==y2==y3:
    print(-1.0)
elif (x1==x2 and y1==y2) or (x1==x3 and y1==y3) or (x2==x3 and y2==y3):
    print(-1.0)
elif ((x3-x1)*(y2-y1)==(y3-y1)*(x2-x1)):
    print(-1.0)
else:


    result_max = max(l1,l2,l3)
    result_min = min(l1,l2,l3)

    print(2*(result_max-result_min))