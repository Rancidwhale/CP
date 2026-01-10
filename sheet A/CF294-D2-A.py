n = int(input())
a = list(map(int, input().split()))
m = int(input())


def solve(p,q):
    p=p-1
    l,r = q-1 , a[p]-q
    if p-1>=0:
        a[p-1] +=l
    if p+1<n:
        a[p+1] +=r
    a[p]=0
    #print(l,r,a)

for _ in range(m):
    x,y = map(int, input().split())
    solve(x,y)

for i in a:
    print(i)