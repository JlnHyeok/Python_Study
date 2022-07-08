'''
f = open('Text2.txt','w')

f.write('12345678910')

f.close()


f = open('loop.txt','a')

for i in range(1,101):

    f.write(f'숫자 {i} ' )

f.close()


file = open('pratice.txt','w')

for i in range(1,6):
    d = f'제{i}의아해가무섭다고그리오.\n'
    file.write(d)

file.close()

file2 = open('pratice.txt','r')

b = file2.read()

file2.close()
print(b)
'''
