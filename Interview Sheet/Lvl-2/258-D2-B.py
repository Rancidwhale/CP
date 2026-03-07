n = int(input())
a = list(map(int, input().split()))

l = 0
while l < n - 1 and a[l] <= a[l + 1]:
    l += 1
if l == n - 1:
    print("yes")
    print(1, 1)
    exit()
r=l
while  r < n - 1 and a[r]>a[r+1]:
    r+=1

a[l:r+1] = reversed(a[l:r+1])
    # print("pass")
if all(a[i] <= a[i+1] for i in range(n-1)):
    print("yes")
    print(l+1, r+1)
else:
    print("no")


'''
3 2 1 4 5
0 1 2 3 4
n=5
l=0
i=1
2<3
i=2
1<2
i=3
4<1 false
r=3
'''   