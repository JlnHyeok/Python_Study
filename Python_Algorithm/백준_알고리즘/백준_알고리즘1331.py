x=[0 for _ in range(37)]
y=[0 for _ in range(37)]
li = [None for _ in range(37)]

for i in range(1,37):
    a = input()
    if a in li:
        print('Invalid')
        exit()
    li[i] = a

    x[i] = a[0]
    y[i] = a[1]



for i in range(1,36):
    if ord(x[i+1]) == ord(x[i])+1:
        if ord(y[i+1]) == ord(y[i]) +2 or ord(y[i+1]) == ord(y[i])-2:
            pass
        else:
            print('Invalid')
            exit()

    elif ord(x[i+1]) == ord(x[i])+2:
        if ord(y[i+1]) == ord(y[i]) +1 or ord(y[i+1]) == ord(y[i]) -1:
            pass
        else:
            print('Invalid')
            exit()

    elif ord(x[i+1]) == ord(x[i])-1:
        if ord(y[i+1]) == ord(y[i]) -2 or ord(y[i+1]) == ord(y[i]) +2:
            pass
        else:
            print('Invalid')
            exit()
    elif ord(x[i+1]) == ord(x[i])-2:
        if ord(y[i+1]) == ord(y[i]) -1 or ord(y[i+1]) == ord(y[i]) +1:
            pass
        else:
            print('Invalid')
            exit()
    else:
        print('Invalid')
        exit()


if ord(x[1]) == ord(x[36]) + 1:
    if ord(y[1]) == ord(y[36]) + 2 or ord(y[1]) == ord(y[36]) - 2:
        pass
    else:
        print('Invalid')
        exit()

elif ord(x[1]) == ord(x[36]) + 2:
    if ord(y[1]) == ord(y[36]) + 1 or ord(y[1]) == ord(y[36]) - 1:
        pass
    else:
        print('Invalid')
        exit()

elif ord(x[1]) == ord(x[36]) - 1:
    if ord(y[1]) == ord(y[36]) - 2 or ord(y[1]) == ord(y[36]) + 2:
        pass
    else:
        print('Invalid')
        exit()
elif ord(x[1]) == ord(x[36]) - 2:
    if ord(y[1]) == ord(y[36]) - 1 or ord(y[1]) == ord(y[36]) + 1:
        pass
    else:
        print('Invalid')
        exit()
else:
    print('Invalid')
    exit()

print('Valid')