n,k = map(int,input().split())
mid =0
if n%2 == 0:
    mid = n/2
else: mid = (n+1)/2

if k > mid:
    k-=mid
    print(int(k*2))
else:
    print(int((k*2)-1))

