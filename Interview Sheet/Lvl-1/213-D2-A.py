n , k = map(int, input().split())
count = 0
flag = True
good =[]
for i in range(0,k+1):
    good.append(str(i))

for _ in range(n):
    a = input()
    for i in good:
            # print(i, flag2)
        if i not in a:
            flag =False
            break
    if flag:
        count+=1
    flag =True
        # print(count,flag2)
print(count)
        




