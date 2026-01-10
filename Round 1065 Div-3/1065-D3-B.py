ans=[]
ans2=[]
k=0
t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    flag = 0
    an = a[-1]
    a0 = a[0]
    min_sum=0
    if an == -1 and a0 == -1:
        an = a0 = 0
        min_sum=0
        flag = 1
    elif an ==-1:
        an = a0
        min_sum=0
        flag = 2
    elif a0 == -1:
        a0 =an
        min_sum=0
        flag = 3
    else:
        min_sum = abs(an-a0)
    
    a[-1] = an
    a[0] = a0
    for i in range(len(a)):
        if a[i]==-1:
            a[i]=0
    ans.append(min_sum)
    ans2.append(a)   
    t-=1
for i in ans2:
    print(ans[k])
    print(*i)
    k+=1


