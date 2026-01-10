t = int(input())
ans = []
while t:
    t-=1
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    max = 0
    if n == 2:
        ans.append(abs(l[0]-l[1]))
    else:
        for i in range(0,n-1,2):
            diff = abs(l[i] -l[i+1])
            if diff > max :
                max = diff
        ans.append(max)
for i in ans:
    print(i)