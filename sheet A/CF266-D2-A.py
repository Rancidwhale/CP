n = int(input())
s = input()

p=s[0]
c=0
for i in s[1:]:
    if i == p:
        c+=1
        continue
    else:
        p = i

print(c)


