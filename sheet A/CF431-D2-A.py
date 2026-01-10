a = list(map(int, input().split()))
s = input()

sum=0
for i in s:
    i=int(i)
    sum+=a[i-1]
print(sum)