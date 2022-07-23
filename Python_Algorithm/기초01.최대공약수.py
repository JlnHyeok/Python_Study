def gcd(a,b):
    while a!=0 and b!=0:
        if a>b: a=a%b
        else : b=b%a

    return a+b

a=list(map(int,input("두개의 값 입력 : ").split()))

print(a)

c = gcd(a[0],a[1])

print(f'최대 공약수 : {c}')

