q = int(input())
ans = []
while q:
    n = int(input())
    s,t = map(str, input().split())
    q-=1
    s =sorted(s)
    t = sorted(t)
    if s==t:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)