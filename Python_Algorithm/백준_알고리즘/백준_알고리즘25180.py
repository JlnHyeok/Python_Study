
# i = 1
#
# while 1:
#     if n/i<=9 and (n%i)%2==0:
#         break
#     else:
#         i+=1

n=int(input())
k = 9
if (n%k)==0:
    ans = (n // k)
elif (n//k)%2==1 and (n%k)%2==1:
    ans = (n // k) + 1
elif (n//k)%2==0:
    ans = (n // k) + 1
else:
    ans = (n // k) + 2

print(ans)
