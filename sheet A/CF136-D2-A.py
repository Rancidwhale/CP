n = int(input())
ans = []

a = list(map(int, input().split()))
b = a.copy()
for i in a:
    b[i-1]=a.index(i)+1

ans.append(b)

for j in ans:
    print(" ".join(map(str,j)))

