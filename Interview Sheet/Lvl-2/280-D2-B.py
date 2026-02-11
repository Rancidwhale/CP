n , l = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)

# print(a)
n1=n2=0

m1=0
if a[0]!=0:
    m1=a[0]
m2=0
if a[-1]!=l:
    m2=l-a[-1]
m=0
# print(m1,m2)
for i in range(1,n):
    cur= a[i]-a[i-1]
    m = max(cur,m)

print(max(m1,m2,m/2))