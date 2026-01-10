def getnext(i,a):
    return a[i+1]

def dist():
    pass

def solve(n,m,arr):
    p=0
    xs1,ys1=0,0
    xs2,ys2=0,0
    if n==1:
        p=4*m
    else :
        for i in range(len(arr)):
            if i==0:
                x,y = arr[i]
                xn,yn = getnext(i,arr)
                p = p + (2 * m )+ (xn-x)+(yn-y)
                xs1=xn
                ys1=y+m
                xs2=x+m
                ys2=yn
            elif i<n-1 :
                pass
                #st1
                x,y = arr[i]
                xn,yn=getnext(i,arr)
                p = p + (y+m-ys1) + (x+m-xs2) + (xn-x)+(yn-y)
                xs1=xn
                ys1=y+m
                xs2=x+m
                ys2=yn
            else:
                pass
                x,y = arr[i]
                p = p + (y+m-ys1) + (x+m-xs2) +2*m
    ans.append(p)
ans =[]
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        x,y = map(int,input().split())
        if i>0:
            x1,y1 = arr[i-1]
            x,y = x+x1,y+y1
        arr.append([x,y])
    #print(arr)
    solve(n,m,arr)
for i in ans:
    print(i)



