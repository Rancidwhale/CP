n = int(input())
l = [1,2,3,4,0]
k=1
ans=0
while n>0:
    if n==9:
        n=n // 10
        ans += 9*k
        k*=10
        continue
    d = int(n%10)
    n= n // 10

    # print("d",d)
    # print("n",n)
    if d in l:
        ans += d*k
        k*=10
        continue
    d = 9-d
    ans += d*k
    k*=10
print(ans)