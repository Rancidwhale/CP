n = int(input())
s = list(map(int,input().split()))
temp = [False]*(n+1)
cur = n
for i in s:
    temp[i]=True
    # print(temp,cur)
    while temp[cur] and cur >0:
        print(cur, end=' ')
        cur-=1
    if not temp[cur]:
        print()
    

    

