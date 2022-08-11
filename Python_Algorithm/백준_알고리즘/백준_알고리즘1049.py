n,m = map(int,input().split())

price_list = [1000, 1000]

for i in range(m):
    a,b = map(int,input().split())
    if a<= price_list[0]:
        price_list[0] = a
    if b<= price_list[1]:
        price_list[1] = b


remain = (n%6)
ans = 0
if price_list[0]<price_list[1]*6:
    if remain*price_list[1]<=price_list[0]:
        ans = remain*price_list[1]
    else:
        ans = price_list[0]
    ans += (n//6)*price_list[0]
else:
    ans = n*price_list[1]

print(ans)