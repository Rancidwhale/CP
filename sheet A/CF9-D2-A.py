y, w = map(int, input().split())

x=max(y,w)
diff=(6-x+1)
num=diff
denom = 6

if num%2==0:
    num=int(num/2)
    denom=int(denom/2)
if num%3==0:
    num=int(num/3)
    denom=int(denom/3)

print(str(num)+"/"+str(denom))