sum=0
timeforprobs = []
for i in range(1,11):
    sum=sum+(i*5)
    timeforprobs.append(sum)
n,k=map(int,input().split())
m=240-k
c=0
for i in timeforprobs:
    if m<i or c==n:
        break
    c+=1

print(c)