n , b, d = map(int, input().split())

a = list(map(int, input().split()))

sum = 0 
count = 0
for i in a:
    if i>b:continue
    sum += i 
    if sum > d:
        count+=1
        sum = 0
    #print(sum,count)
print(count)