import sys
n = int(input())
 
cities = list(map(int,input().split()))
 
cost = []
mincost = sys.maxsize
maxcost = -sys.maxsize-1
 
for i in range(n):
    mincost = sys.maxsize
    maxcost = -sys.maxsize-1
    if i:
        mincost = min(mincost,cities[i]-cities[i-1])
        maxcost = max(maxcost,cities[i]-cities[0])
    if i<n-1:
        mincost = min(mincost,cities[i+1]-cities[i])
        maxcost = max(maxcost,cities[n-1]-cities[i])
    cost.append([mincost,maxcost])
for i in cost:
    print(" ".join(map(str,i)))