import math

n,kim,lim = map(int,input().split())
cnt = 0

while kim != lim:
    kim = math.ceil(kim/2)
    lim = math.ceil(lim/2)
    cnt+=1

print(cnt)


# 시간초과
# match = [0 for _ in range(n)]
# match[kim-1] = kim
# match[lim-1] = lim

# while kim in match:
#     n//=2
#     for i in range(n):
#        if match[i]>match[i+1]:
#            match.pop(i+1)
#            if kim not in match:
#                break
#        else:
#            match.pop(i)
#            if kim not in match:
#                break
#     cnt+=1
