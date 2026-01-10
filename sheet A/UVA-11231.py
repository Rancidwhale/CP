# w b w b w b w b w 9
# b w b w b w b w b 8
# w b w b w b w b w 7
# b w b w b w b w b 6
# w b w b w b w b w 5
# b w b w b w b w b 4
# w b w b w b w b w 3
# b w b w b w b w b 2
# w b w b w b w b w 1 
# 9 8 7 6 5 4 3 2 1

def solve(n,m,c):
        if c==1:
            return int(((n-7)*(m-7)+1)/2)
        else:
            return int((n-7)*(m-7)/2)

ans =[]
while True:
    n,m,c = map(int,input().split())
    if n+m+c==0:
         break
    ans.append(solve(n,m,c))

for i in ans:
     print(i)  # Output: 36 36 36 36 36 36
