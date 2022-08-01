n = int(input())
ser = [0 for _ in range(n)]
k = [0 for _ in range(n)]
for i in range(n):
    ser[i] = input()

ser = sorted(ser,key=len)

for i in range(n):
    for char in ser[i] :
        if char in '0123456789':
            k[i]+=int(char)
    print(k)

dic={}

for i,v in enumerate(k):
    dic[v]=ser[i]

i=0
while 1:
    if len(ser[i]) == len(ser[i+1]) and k[i]>k[i+1]:
        ser[i],ser[i+1] = ser[i+1],ser[i]

    i+=1
    if i==n-1:
        break

print(ser)
print(dic)