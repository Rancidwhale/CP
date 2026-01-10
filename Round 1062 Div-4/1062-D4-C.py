'''
0 1 2 1 3 2 1 1
0 1 1 2 2 1 1 3
0 1 1 2 1 1 2 3
0 1 1 1 1 2 2 3


0 2 2    1 1 3 1 1 
0 2 2    1 1 1 1 3

0 1 1 1 1 2 2 3

2 5 3 1 7
2    5 3 1 7
2    1 3 5 7
1 2 3 5 7

'''
t = int(input())
ans = []
while t:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))

    evens = []
    odds =[]
    for i in a :
        if i%2==0:
            evens.append(i)
        else:
            odds.append(i)

    if not len(evens):
        ans.append(odds)
        continue
    if not len(odds):
        ans.append(evens)
        continue
    evens =sorted(evens)
    odds = sorted(odds)
    l = m = 0
    small =[]
    while l<len(evens) and m< len(odds):
        if evens[l]<odds[m]:
            small.append(evens[l])
            l+=1
        else:
            small.append(odds[m])
            m+=1
    if l == len(evens):
        while m< len(odds):
            small.append(odds[m])
            m+=1
    else:
        while l<len(evens):
            small.append(evens[l])
            l+=1
    ans.append(small)


for i in ans:
    print(' '.join(map(str,i)))