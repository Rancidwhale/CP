n = int(input())
h = list(map(int,input().split()))
sec = 0
for i in range(0,n):
    # print("i",i)
    cur=1
    p=i-1
    q=i+1
    c = h[i]
    # print(p,q,c)
    if p>=0:
        while p>-1:
            # print(p,cur)
            if h[p]<=h[p+1]:
                p-=1
                cur+=1
            else:
                break
        # print("in left",cur, p)
    if q<n:
        while q<n:
            # print(q,cur)
            if h[q]<=h[q-1]:
                q+=1
                cur+=1
            else:
                break
            # print("q",q,"cur",cur)
            if q>=n:
                break
        # print("in right",cur,q)
    sec = max(cur,sec)
    # print("max",sec)
print(sec)