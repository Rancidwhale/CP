shift = input()
str = input()

a = "qwertyuiop"
b = "asdfghjkl;"
c = "zxcvbnm,./"
ans = ""

def solve(ch, l):
    i = l.index(ch)
    if shift == "L":
        return l[i+1]
    else:
        return l[i-1]

for i in str:
    if i in a:
        s = solve(i,a)
    elif i in b:
        s = solve(i,b)
    else:
        s = solve(i,c)
    ans+=s

print(ans)
