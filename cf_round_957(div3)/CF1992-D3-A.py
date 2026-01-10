n = int(input())
mat =[]
for i in range(n):
    a = list(map(int, input().split()))
    mat.append(a)
    
for l in mat:
    a,b,c = l[0],l[1],l[2]
    k=5
    while k:
        if a<=b and a<=c:
            a+=1
        elif b<=c and b<=a:
            b+=1
        elif c<=a and c<=b:
            c+=1
        k-=1
    print(a*b*c)
