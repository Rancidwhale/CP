t = int(input())
ans = []
mat1=[]
mat2 = []
for _ in range(t):
    n,k = map(int, input().split())
    l = list(map(int,input().split()))
    mat1.append([n,k])
    mat2.append(l)

for i in range(t):
    [n,k] = mat1[i]
    l = mat2[i]
    l.sort()
    step =0
    while len(l)!=1:
        if l[0]==1:
            l.pop(0)
            l[-1]+=1
            step+=1
        elif l[0] == 2:
            l.pop(0)
            l[-1] += 2
            step += 3
        else:
            q=l.pop(0)
            l[-1]+=q
            step = step + (q*2) - 1
    print(step)

