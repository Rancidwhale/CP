'''
1 0 0 1
1 0 1
1 1
0
1011
1 0
1

1001
1011

'''
def isodd(n):
    if n%2!=0:
        return True
    else:
        return False

def setflag(x,y):
    if isodd(x) and not isodd(y):
        return 1
    elif not isodd(x) and isodd(y):
        return 2
    else:
        return 0
t = int(input())
ans = []
while t:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    onesa=0
    onesb=0
    for i in range(n):
        if a[i]==1:
            onesa+=1
        if b[i]==1:
            onesb+=1
    
    for i in range(n):
        s = [a[i],b[i]]
        j=i+1
        if j%2 != 0:
            if s == [1,0]:
                if not isodd(onesa):
                    a[i],b[i] = b[i],a[i]
                    onesa-=1
                    onesb+=1
            elif s == [0,1]:
                if not isodd(onesa):
                    a[i],b[i] = b[i],a[i]
                    onesa+=1
                    onesb-=1
        else:
            if s == [1,0]:
                if not isodd(onesb):
                    a[i],b[i] = b[i],a[i]
                    onesa-=1
                    onesb+=1
            elif s == [0,1]:
                if not isodd(onesb):
                    a[i],b[i] = b[i],a[i]
                    onesa+=1
                    onesb-=1
        # print("flag",flag)
    flag = setflag(onesa,onesb)

    if flag == 0 :
        ans.append("Tie")
    elif flag ==1:
        ans.append("Ajisai")
    else:
        ans.append("Mai")
        
    t-=1
for i in ans:
    print(i)