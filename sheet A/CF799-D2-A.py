n, t, k, d = map(int, input().split())

def do(x,y):
    if x%y != 0:
        return int(x/y)+1
    return int(x/y)

req = do(n,k)
time = req * t
time-=t

if time>d:
    print("YES")
else:
    print("NO")