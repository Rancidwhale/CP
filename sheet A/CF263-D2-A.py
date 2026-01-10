p,q=0,0
b=[]
for i in range(5):
    a = list(map(int, input().split()))
    b.append(a)
for i, row in enumerate(b):
    for j, value in enumerate(row):
        if value == 1:
            p,q =i, j
if p>2:
    p=p-2
else:
    p=2-p
if q>2:
    q=q-2
else:
    q=2-q
print(p+q)