n,k = map(int, input().split())
even = False
mid = 0
if n%2==0:
    even = True
    mid = int(n/2)
else:
    even =False
    mid = int(n/2) +1 

if k<=mid:    
    print((k*2)-1)
else:
    print((k-mid)*2)
    
#         1 2 3  
# 1 2 3 4 5 6 7
# 1 3 5 7 2 4 6