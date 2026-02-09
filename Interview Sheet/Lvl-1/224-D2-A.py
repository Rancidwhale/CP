s1 = input()
s2 = input()
a=b=0
id = s1.index('|')
a = len(s1[:id])
a1 = s1[:id]
b = len(s1[id+1:])
b1 = s1[id+1:]
d = len(s2)
# print(a,b,d)
yea = True
if a>b:
    diff = a-b
    if diff<=d:
        d-=diff
        b1+=s2[:diff]
        # print(d)
        # print(a1,b1)
        if d%2==0:
            if d != 0:
                s2=s2[diff:]
                d=len(s2)
                diff = d//2
                # print(s2)
                # print(diff)
                a1 += s2[:diff]
                b1 += s2[diff:]
                # print(a1,b1)
        else:
            print("Impossible")
            yea = False
    else:
        print("Impossible")
        yea = False
elif b>a:
    diff = b-a
    if diff<=d:
        d-=diff
        a1+=s2[:diff]
        # print(d)
        # print(a1,b1)
        if d%2==0:
            if d != 0:
                s2=s2[diff:]
                d=len(s2)
                diff = d//2
                # print(s2)
                # print(diff)
                a1 += s2[:diff]
                b1 += s2[diff:]
                # print(a1,b1)
        else:
            print("Impossible")
            yea=False
    else:
        print("Impossible")
        yea = False
else:
    if d%2==0:
        if d != 0:
            diff = d//2
            # print(s2)
            # print(diff)
            a1 += s2[:diff]
            b1 += s2[diff:]
            # print(a1,b1)
    else:
        print("Impossible")
        yea=False
if yea:
    print(a1+'|'+b1)