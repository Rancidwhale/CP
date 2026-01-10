n =int(input())
mat=[]
for _ in range(n):
    mat.append(list(map(int,input().split())))
c=0
for i in range(n):
    ck1=mat[i]
    for j in range(n):
        if i==j:
            continue
        ck2=mat[j]
        if ck1[1]==ck2[0]:
            c+=1
print(c)