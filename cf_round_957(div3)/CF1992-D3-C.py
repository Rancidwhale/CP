t = int(input())
mat = []
for _ in range(t):
    l = list(map(int,input().split()))
    mat.append(l)

for [n,m,k] in mat:
    temp = n
    temp2=1
    ans = []
    for i in range(n):
        if temp<=m:
            ans.append(temp2)
            temp2+=1
            temp-=1
        else:
            ans.append(temp)
            temp-=1
    print(" ".join(map(str,ans)))