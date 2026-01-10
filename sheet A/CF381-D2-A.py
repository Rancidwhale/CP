n= int(input())
a = list(map(int,input().split()))
s = 0
d = 0
pt1=0
pt2=n-1
turn = True
while pt1<=pt2:
    if a[pt1]>a[pt2]:
        if turn:
            s+=a[pt1]
            pt1+=1
            turn = False

        else:
            d+=a[pt1]
            pt1+=1
            turn = True

    else:
        if turn:
            s+=a[pt2]
            pt2-=1
            turn = False

        else:
            d+=a[pt2]
            pt2-=1
            turn = True


print(s,d)


