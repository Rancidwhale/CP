def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
ans = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
t = int(input())
while t:
    t-=1
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    for i in primes:
        flag =0
        # print("i : ",i)
        for j in s:
            num = gcd(i,j)
            # print("j : ",j)
            if num ==1:
                flag = 1
                break
            # print("num : ",num)
            # print("flag : ",flag)
        if flag == 1:
            ans.append(i)
            break
    if flag != 1:
        ans.append(-1)

for i in ans:
    print(i)