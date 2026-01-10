n = int(input())
c = list(map(int, input().split()))

c.sort()

def solve(c,n):
    t1=c[0:-1]
    t2=[]
    t2.append(c[-1])
    a=sum(t1)
    b=c[-1]
    while a>=b:
        p=t1.pop()
        a-=p
        b+=p
        t2.append(p)
    return len(t2)
print(solve(c,n))