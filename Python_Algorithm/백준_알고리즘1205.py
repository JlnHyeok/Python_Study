N,Score,P = map(int,input().split())
Score_list=[]

if N==0:
    print(1)

else:
    Score_list = sorted(list(map(int, input().split())),reverse=True)


    if N==P and Score <= Score_list[N-1]:
        print(-1)
        exit()

    Score_list.append(Score)

    Score_list = sorted(Score_list,reverse=True)

    for i in range(P):
        if Score >= Score_list[i]:
            break

    i+=1
    if i>P:
        print(-1)
    else:
        print(i)