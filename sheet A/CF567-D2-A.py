# import sys
# n = int(input())

# cities = list(map(int,input().split()))

# cost = []
# def getmin(cities,i):
#     if cities[i]<0:
#         if i<n-1:
#             if cities[i+1]>0:
#                 rcost = cities[i+1] + abs(cities[i])
#             else:
#                 rcost = abs(cities[i]-cities[i+1])
#             if i==0: return rcost
#         lcost = abs(cities[i-1]-cities[i])
#         if i==n-1: return lcost
#         return min(lcost,rcost)
#     if cities[i]>=0:
#         if i>0:
#             if cities[i-1]<0:
#                 lcost = cities[i] + abs(cities[i-1])
#             else:
#                 lcost = abs(cities[i]-cities[i-1])
#             if i==n-1: return lcost
#         rcost = abs(cities[i]-cities[i+1])
#         if i==0: return rcost
#         return min(lcost,rcost)
# def getmax(cities,i):
#     if cities[i]<0:
#         lcost = abs(cities[0]-cities[i])
#         if cities[n-1]>0:
#             rcost = cities[n-1] + abs(cities[i])
#         else:
#             rcost = abs(cities[i]-cities[n-1])
#         return max(lcost,rcost)
#     if cities[i]>=0:
#         rcost = abs(cities[i]-cities[n-1])
#         if cities[0]<0:
#             lcost = cities[i] + abs(cities[0])
#         else:
#             lcost = abs(cities[i]-cities[0])
#         return max(lcost,rcost)

# mincost = sys.maxsize
# maxcost = -sys.maxsize-1
# for i in range(n):
#     mincost = getmin(cities,i)
#     maxcost = getmax(cities,i)
#     cost.append([mincost,maxcost])


# for i in cost:
#     print(" ".join(map(str,i)))



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

