n = int(input())
for _ in range(n):
    m=int(input())
    min = 10
    while m:
        r = m%10
        if r<min:
            min =r
        m = int(m/10)
    print(min)
