r1,r2 = map(int, input().split())
c1,c2 = map(int, input().split())
d1,d2 = map(int,input().split())

op = [1,2,3,4,5,6,7,8,9]
got = False
for i in op:
    cur = op.copy()
    c= r1 - i 
    if c<=0 or c == i or c>9:
        continue
    cur.remove(i)
    # print(i,c)
    cur.remove(c)
    # print(cur)
    for j in cur:
        cur2 = cur.copy()
        # print(j)
        d = r2 - j
        # print("d",d)
        if d<=0 or d not in cur2 or d>9 or j == d:
            continue
        cur2.remove(j)
        # print(j,d)
        cur2.remove(d)
        # print(cur2)

        if(i+j == c1 and c+d == c2 and i+d == d1 and j+c == d2):
            got = True
            row1 = [i,c]
            row2 = [j,d]
        elif(c+j == c1 and i+d == c2 and i+j == d2 and c+d == d1):
            got = True
            row1 = [c,i]
            row2 = [j,d]
        elif(i+d == c1 and c+j == c2 and i+j == d1 and c+d == d2):
            got = True
            row1 = [i,c]
            row2 = [d,j]
        elif(c+d == c1 and i+j == c2 and c+j == d1 and i+d == d2):
            got = True
            row1 = [c,i]
            row2 = [d,j]

if got:
    print(*row1)
    print(*row2)
else:
    print(-1)
