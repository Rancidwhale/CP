k, r = map(int, input().split())

n=0
d=k%10
c=2
if d==0:
    print(1)
else:
    while d!=r:
        t = k*c
        d = t%10
        c+=1
        #print(t,d,c)
        if t%10==0:break
    print(c-1)

