n = int(input())
s = input()
ans = ''
if n%2 == 0:
    ans += s[0]
    for i in range(1,n):
        if i%2==0:
            ans = s[i]+ans
        else:
            ans = ans + s[i]
else:
    ans += s[0]

    for i in range(1,n):
        if i%2 == 0:
            ans = ans + s[i]
        else:
            ans = s[i]+ans
print(ans)
