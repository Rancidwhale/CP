# n=7 
# k=3 
# l=2 
# r=4
# [1, 2, 1, 2, 3, 2, 1]
# n = 1
# k = 1
# l = 1
# r = 1 
# [5]

# n = 5
# k = 2
# l = 2
# r = 3
# [1,2,1,3,2] 
# [0,1,2,3,4]
# b,c = 0,1
'''
fixing r

calculate one point j
'''
# 1
# 7 3 2 4
# 1 2 1 2 3 2 1
# 0 1 2 3 4 5 6
# l and r :  2   4
# window-len:  2
# Window:  [1, 2]  distict:  2
# win len:  2 sp :  1
# count:  0
# Window:  [1, 2, 1]  distict:  2
# win len:  3 sp :  2
# count:  0
# Window:  [1, 2, 1, 2]  distict:  2
# win len:  4 sp :  3
# count:  0
# l and r :  2   4
# window-len:  2
# Window:  [2, 1]  distict:  2
# win len:  2 sp :  2
# count:  0
# Window:  [2, 1, 2]  distict:  2
# win len:  3 sp :  3
# count:  0
# Window:  [2, 1, 2, 3]  distict:  3
# win len:  4 sp :  4
# count:  1
# l and r :  2   4
# window-len:  2
# Window:  [1, 2]  distict:  2
# win len:  2 sp :  3
# count:  1
# Window:  [1, 2, 3]  distict:  3
# win len:  3 sp :  4
# count:  2
# Window:  [1, 2, 3, 2]  distict:  3
# win len:  4 sp :  5
# count:  3
# l and r :  2   4
# window-len:  2
# Window:  [2, 3]  distict:  2
# win len:  2 sp :  4
# count:  3
# Window:  [2, 3, 2]  distict:  2
# win len:  3 sp :  5
# count:  3
# Window:  [2, 3, 2, 1]  distict:  3
# win len:  4 sp :  6
# count:  4
# l and r :  2   4
# window-len:  2
# Window:  [3, 2]  distict:  2
# win len:  2 sp :  5
# count:  4
# Window:  [3, 2, 1]  distict:  3
# win len:  3 sp :  6
# count:  5
# 5

t = int(input())
ans =[]
while t:
    t-=1
    n,k,l,r = map(int, input().split())
    a = list(map(int, input().split()))
    count =0
    if n==1:
        count = 1
    else:
        for i in range(n-k+1):
            # print("i: ",i)
            if i + l -1 <= n:
                x = i + l -1
            if i + r -1<n:
                y = i + r -1
            elif x<=n:
                y=n-1
            # print("l and r : ",l," ", r)
            # print("x and y : ",x," ", y)
            flag = True
            while flag and x<=y and x+1<=n and y+1<=n:
                window = a[i:y+1]
                distinct = len(set(window))
                # print("Window: ",window," distict: ",distinct)
                # print("X : ",x,"Y : ",y)
                if distinct < k:
                    flag = False
                    continue
                elif distinct == k:
                    count +=1
                else:
                    pass
                if x==y:
                    flag =False
                    continue
                window = a[i:x+1]
                distinct = len(set(window))
                # print("Window: ",window," distict: ",distinct)
                # print("X : ",x,"Y : ",y)
                if distinct<k:
                    pass
                elif distinct == k:
                    count +=1
                else:
                    flag = False
                x+=1
                y-=1
                # print("count: ",count)
                # print("flag: ",flag)
    ans.append(count)

for i in ans:
    print(i)