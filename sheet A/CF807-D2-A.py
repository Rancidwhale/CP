n = int(input())
ans=0
l=['','maybe', 'unrated', 'rated']
temp=4127
for _ in range(n):
    a,b = map(int,input().split())
    if a != b:
            ans=3
    if ans <2:  
            if a<=temp:
                ans=1
            else: ans=2

    temp=a
print(l[ans])
    