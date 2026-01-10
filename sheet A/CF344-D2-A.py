n=int(input())
a=[]
for _ in range(n):
    a.append(input())
p = a[0]
c=1
for i in a[1:]:
    if i!=p:
        c+=1
    p=i

    
print(c)
