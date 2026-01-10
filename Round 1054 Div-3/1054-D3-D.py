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
        if an == 0 or bn ==0:
            ans.append(0)
        
        elif an ==1:
            if a[0] == 0:
                ans.append(0)
            else:
                ans.append(min ( b[0], abs( n -b[0]-1)))
        elif bn==1:
            if b[0] == 0:
                ans.append(0)
            else:
                ans.append(min( a[0], abs( n-a[0]-1 )))
        else:
            if an%2 == 0:
                median_index = an//2 - 1
                median = a[median_index]
                st = median - median_index
                sp = median + an//2
                costa = calculate_cost(st,sp,a,s)
            else:
                median_index = an//2
                median = a[median_index]
                st = median - median_index
                sp = median + median_index
                costa = calculate_cost(st,sp,a,s)
            if bn%2 == 0:
                median_index = bn//2 -1
                median =b[median_index]
                st = median - median_index
                sp =median + bn//2
                costb = calculate_cost(st,sp,b,s)
            else:
                median_index = bn//2
                median = b[median_index]
                st = median - median_index
                sp = median + median_index
                costb = calculate_cost(st,sp,b,s)
            ans.append(min(costa,costb))
    else:
        ans.append(0)

for i in ans:
    print(i)




# "baabbabba"                
# "1 2 5 8"
# "0 3 4 6 7"
