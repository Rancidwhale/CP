n,k = map(int,input().split())
segments = []
for _ in range(n):
    l,r = map(int,input().split())
    segments.append([l,r])
[l,r] = segments[0]
p = r-l
for i in range(1,n):
    [l1,r1] = segments[i-1]
    [l2,r2] = segments[i]
    [l3,r3] = segments[i+1]
    pass

'''
1 2
3 3
4 7


'''