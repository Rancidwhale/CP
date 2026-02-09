import sys
n = int(input())
d = input()
pos = list(map(int, input().split()))
m = sys.maxsize
collide=False
if n==2: n+=1

for i in range(1,n-1):
    c = d[i]
    if c == 'R':
        if d[i+1]=='L':
            dist = abs(pos[i]-pos[i+1])
            m = min(dist,m)
            collide = True
    elif c == 'L':
        if d[i-1]=='R':
            dist = abs(pos[i]-pos[i-1])
            m = min(dist,m)
            collide = True
if collide:
    print(m//2)
else:
    print(-1)    