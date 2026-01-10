n , k = map(int,input().split())
a = list(map(int, input().split()))
k-=1
sc = a[k]

if a[k]>0:
    while a[k]==sc : 
        k+=1
        if k>n-1:
            break
    print(k)
elif a[k]<1:
    while a[k]<1 and k>=0:
        
        k-=1
    print(k+1)