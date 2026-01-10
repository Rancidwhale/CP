n,h = map(int, input().split())
w = 0
l = list(map(int, input().split()))
for i in l:
    if i > h :
        w += 2
    else:
        w += 1
print(w)
