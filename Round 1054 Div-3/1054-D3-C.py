t = int(input())
ans = []
while t:
    t-=1
    n ,k = map(int,input().split())
    l = list(map(int,input().split()))
    miss = 0

    freq = [0] * (n+1)
    for num in l:
        freq[num] += 1

    for i in range(k):
        if freq[i] == 0:
            miss += 1
         
    c = freq[k]
    # for i in range(int(k)):
    #     if i not in l:
    #         miss+=1
    # c = l.count(int(k))
    ans.append(max(c,miss))

for i in ans:
    print(i)