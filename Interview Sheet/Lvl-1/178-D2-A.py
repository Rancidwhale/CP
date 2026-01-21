n = int(input())
x=0
while n:
    t = input()
    if t == 'X++' or t =='++X':
        x+=1
    else:
        x-=1
    n-=1
print(x)