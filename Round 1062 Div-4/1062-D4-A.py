n=int(input())
ans =[]
while n:
    l = list(map(int,input().split()))
    s =set(l)
    if len(s)==1:
        ans.append("YES")
    else:
        ans.append("NO")
    n-=1

for i in ans:
    print(i)