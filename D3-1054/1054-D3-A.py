t = int(input())
ans = []
while t:
    n = int(input())
    l = list(map(int,input().split()))
    zero = l.count(0)
    neg_one = l.count(-1)
    op = 0
    if neg_one>0:
        if neg_one % 2 == 0:
            pass
        else: op +=2
    if zero > 0:
        op += zero
    ans.append(op)
    t-=1
for i in ans:
    print(i)