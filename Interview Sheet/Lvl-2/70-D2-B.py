n = int(input())
c = "ROYGBIV"
c1 = "ROYG"
c2 = "RVIB"
c3 = "GVI"
if n==7: print(c)
elif n% 8 == 0:
    print((c1+c2)*(n//8))
else:
    s = (c1+c2)*(n//8)
    p = n%8
    if p ==4:
        s+=c1
    elif p<4:
        # c1=c1[::-1]
        s+=c3[0:p]
    elif p>4:
        s+=c1
        c2=c2[::-1]
        s+=c2[0:p-4]

    print(s)
