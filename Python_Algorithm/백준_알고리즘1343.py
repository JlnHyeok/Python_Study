str = input()

a = str.split('.')
for i in a:
    if i.count('X')%2 !=0:
        print(-1)
        exit()

# a = a.replace('x','A',4)

for k in range(len(a)):
    if 'XXXX' in a[k]:
        a[k]=a[k].replace('XXXX','AAAA')
    if 'XX' in a[k]:
        a[k]=a[k].replace('XX','BB')

print('.'.join(a))