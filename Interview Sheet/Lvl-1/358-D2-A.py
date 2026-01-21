n,m = map(int, input().split())
# print(int((n+m)%5))
if int((n+m)%5) == 0:
    div= n+m
else:
    div = n+m - int((n+m)%5)
# print("div",div)
if n>=m:
    max = n
    min = m
else:
    max = m
    min = n
count = 0

for i in range(5,div+1,5):
    # print(i)
    if i <=min:
        count += i-1
        # print("less",count)
    else:
        if i<= max:
            count +=min
            # print("1 less",count)
        else:
            p = i - max
            if p<=min:
                count+=min-p+1
                # print("no less",count)
print(count)
# print("max",max)
# print(p)
# for i in range(1,p+1):
#     for j in range(5,max+1,5):
#         if i>j:
#             continue
#         else:
#             # print("j",j)
#             # print("i",i,"i^",j-i)
#             if j-i <= q and j-i !=0:
#                 count+=1
#             # print(count)

# print(count)
