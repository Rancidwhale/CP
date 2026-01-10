n = int(input())
str = input()
a=0
d=0
for i in str:
    if i=='A':
        a+=1
    else:
        d+=1

if a>d:
    print('Anton')
elif d>a:
    print('Danik')
else:
    print('Friendship')