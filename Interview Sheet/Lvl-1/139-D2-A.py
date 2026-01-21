n = int(input())
t = int(input())
b = 7-t
ans = True
def gettb(q):
    [a,b]=q
    # print("q",q)
    if q in [[1,2] , [1,5] , [2,6] , [5,6]]:
        return [3,4]
    elif q in [[1,3] , [1,4] , [3,6] , [4,6]]:
        return [2,5]
    else:
        return [1,6]
for _ in range(n):
    s1,s2 = map(int,input().split())
    [t1,b1]= gettb(sorted([s1,s2]))
    # print("t:",t,"b",b)
    # print("s1:", s1, "s2:", s2)
    # print("t1:", t1, "b1:", b1)
    
    if sorted([t,b]) != [t1,b1]:
        ans = False
if ans:
    print("YES")
else:
    print("NO")