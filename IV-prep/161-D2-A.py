n=5
for q in range(5):
    a = list(map(int,input().split()))
    if 1 in a:
        i = a.index(1)
        res = abs(i+1-3) + abs(q+1-3)

print(res)