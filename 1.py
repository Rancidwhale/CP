t =  int(input())
days=[]
while t:
    t-=1
    a = list(map(int,input().split()))
    n=a[0]
    a=a[1:]
    s= sum(a)
    p=int(n/s)
    if p>0:
        d = p*3
        left = n%s
        for i in a:
            if left<=0:
                break
            left -=i
            d+=1
            
        days.append(d)
    else:
        d=0
        left = n
        for i in a:
            if left<=0:
                break
            left -=i
            d+=1
            
        days.append(d)
for d in days:
    print(d)

