n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
ra = a[::-1]
d = {}
v,p = 0,0

mapped = {}
for i in range(n):
    mapped[a[i]]=i
for i in b:
    
    if i in d.keys():
        v += d[i][0]
        p += d[i][1]
    else:
        f,r = 0,0
        idx = mapped[i]
        f = idx+1
        r = n - idx 
        d[i]= [f,r]
        v+=f
        p+=r

print(v,p)

