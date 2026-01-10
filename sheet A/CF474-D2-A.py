c = input()
s =input()

if c == "R":
    a=-1
else:
    a=1
keys = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
ans = ""
def solve(keys,s,a):
    global ans
    for i in s:
        index = keys.index(i)
        ans += keys[index+a]
    return ans

print(solve(keys,s,a))