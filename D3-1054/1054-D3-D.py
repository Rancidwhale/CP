def calculate_cost(st,sp,a,s):
    i=0
    sum=0
    for k in range(st,sp+1):
        sum += abs(k - a[i])
        i+=1
    return sum
 
 
t = int(input())
ans = []
while t:
    t-=1
    n = int(input())
    s = input()
    a = []
    b = []
    an,bn=0,0
    if n>2:
        for i in range(n):
            if s[i] == 'a':
                a.append(i)
                an+=1
            else:
                b.append(i)
                bn+=1
        # grouping a
 
        if an >2  and an%2 == 0:
            mpos = an//2 
            median = a[mpos]
            mid = int(an/2)
            st = median - int(an/2)
            sp = median + int(an/2) -1
            costa = calculate_cost(st,sp,a,s)
        elif an==2:
            mpos = an//2 
            median = a[mpos]
            st = median - 1
            sp = median 
            costa = calculate_cost(st,sp,a,s)
        else:
            mpos = an//2 
            median = a[mpos]
            st = median - int(an/2)
            sp = median + int(an/2)
            costa = calculate_cost(st,sp,a,s)
        
        #grouping b
        if bn>2 and bn%2 == 0:
            mpos = bn//2 
            median = b[mpos]
            st = median - int(bn/2)
            sp = median + int(bn/2)-1
            costb = calculate_cost(st,sp,b,s)
        elif bn==2:
            mpos = bn//2 
            median = b[mpos]
            st = median - 1
            sp = median 
            costb = calculate_cost(st,sp,b,s)
        else:
 
            mpos = bn//2 
            median = b[mpos]
            st = median - int(bn/2)
            sp = median + int(bn/2)
            costb = calculate_cost(st,sp,b,s)
        ans.append(min(costa,costb))
    else:
        ans.append(0)
    
for i in ans:
    print(i)