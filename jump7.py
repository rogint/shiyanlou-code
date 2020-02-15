a = 0
while a<100:
    a += 1
    v1=a%7
    v2=a%10
    v3=a//10
    if v1 == 0 or v2 == 7 or v3==7:
        continue
    print(a)

