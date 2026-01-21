n = int(input())
sx,sy,sz=0,0,0
while(n):
    x,y,z = map(int,input().split())
    sx+=x
    sy+=y
    sz+=z
    n-=1
if sz==sy==sx==0:
    print("YES")
else:
    print("NO")