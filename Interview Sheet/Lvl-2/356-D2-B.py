n,a = map(int,input().split())

t = list(map(int, input().split()))

dis = max(a-1,n-a)
id = a-1
c=0
if t[id]==1:c+=1
for i in range(1,dis+1):
    # print(i, id-i, id+i)
    if id-i >=0 and id+i<n:
        if t[id-i]==1 and t[id+i]==1:
            c+=2
            # print(c)
            continue
        else:
            # print(c)
            continue
    if id+i<n:
        if t[id+i]==1:
            c+=1
    if id-i >=0:
        if t[id-i]==1:
            c+=1
    # print("C",c)
print(c)