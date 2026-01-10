n = int(input( ))
a = list(map(int, input().split( )))
un=0
cops = []
for i in a:
    if i==-1:
        if not cops:
            un+=1
        if cops:cops.pop()

    else:
        [cops.append(1) for _ in range(i)]

print(un)
