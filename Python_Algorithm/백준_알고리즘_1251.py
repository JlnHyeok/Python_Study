str = input()

ans=[]

for i in range(1,len(str)-1):
    for j in range(i+1,len(str)):
        ans.append(str[:i][::-1]+str[i:j][::-1]+str[j:][::-1])
ans=sorted(ans)

print(ans[0])
