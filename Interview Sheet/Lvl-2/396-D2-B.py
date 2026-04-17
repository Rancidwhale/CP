n = int(input())
a = list(map(int,input().split()))

a.sort()
got = False
for i in range(0,n-3+1):
    x,y,z = a[i],a[i+1],a[i+2]
    if x+y > z:
        got = True
        print("Yes")
        break
if not got:
    print("No")