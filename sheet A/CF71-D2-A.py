n = int(input())
ans =[]
for _ in range(n):
    s = input()
    if len(s) > 10 : 
        st = s[0]+(str(len(s)-2))+s[-1]
        ans.append(st)
    else:
        ans.append(s)

for a in ans:
    print(a)