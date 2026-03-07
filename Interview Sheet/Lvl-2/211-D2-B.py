n,k = map(int,input().split())
h = list(map(int,input().split()))

cursum = sum(h[:k])
minsum = cursum
j=0
for i in range(k,n):
    cursum = cursum - h[i-k] + h[i]
    if cursum < minsum:
        minsum = cursum
        j=i-k+1


print(j+1)



