n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.pop(0)
b.pop(0)
a.sort()
b.sort()
got =True
for i in range(1,n+1):
    if i in a or i in b:
        pass
    else:
        got=False
        break
if got==True:
    print("I become the guy.")
else: print("Oh, my keyboard!")