n,x = map(int, input().split())
c=0
for _ in range(n):
    op , num = map(str, input().split())
    if op == '+':
        x+=int(num)
    else:
        if int(num) > x :
            c+=1
        else :
            x-=int(num)
        
print(x, c)