n = int(input())
a = list(map(int,input().split()))
p = set(a)
p = list(p)
p.sort()

if len(p)>3: 
    print("NO")
else:    
    if len(p)==3:
        [a,b,c]=p
        # print(abs(a-b),abs(b-c))
        if abs(a-b)==abs(b-c):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
