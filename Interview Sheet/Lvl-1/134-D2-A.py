n,k = map(int,input().split())
y = list(map(int, input().split()))
n = len(y)
for i in range(n):
    if (i+1)%2==0 and y[i]>0 and k>0:
        if i==n-1:
            if y[i]-1 > y[i-1]:
                y[i]-=1
                k-=1
        else:
            if y[i]-1 > y[i-1] and y[i]-1 > y[i+1]:
                y[i]-=1
                k-=1
print(*y)