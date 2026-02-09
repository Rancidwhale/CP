n=4
s = []
for _ in range(n):
    s.append(input())
got = False
for i in range(3):
    for j in range(3):
        ch = s[i][j]
        count = 0
        if s[i][j+1] == ch:
            count+=1
        if s[i+1][j] == ch:
            count+=1
        if s[i+1][j+1] == ch:
            count+=1
        if count != 1:
            got=True

if got:
    print("YES")
else:
    print("NO")