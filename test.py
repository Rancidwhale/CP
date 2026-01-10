
c = 0

def stepcount(n, ways,curSum):
    global c 
    print(ways,curSum,c)

    if curSum==n:
        c+=1
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    if curSum+1<=n:
        ways.append(1)
        curSum+=1
        stepcount(n, ways.copy(),curSum)
    
    print(ways,curSum,c)

    

    if curSum+2<=n:
        ways.append(2)
        curSum+=2
        stepcount(n, ways.copy(),curSum)

    

k = stepcount(3,[],0)
