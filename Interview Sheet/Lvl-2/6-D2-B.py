n,m,ch = input().split()
n=int(n)
m = int(m)
tab = []
for _ in range(n):
    tab.append(input())
count=0
adj = []
for i in range(n):
    if ch in tab[i]:
        for j in range(m):
            if tab[i][j] == ch:
                if j-1>=0:
                    c = tab[i][j-1]
                    if c != ch and c !='.' and c not in adj:
                        count+=1
                        adj.append(c)
                        # print("left ++")
                        # print(i,j)
                if j+1<m:
                    if tab[i][j+1] != ch and tab[i][j+1] !='.' and tab[i][j+1] not in adj:
                        count+=1
                        adj.append(tab[i][j+1])
                        # print("right++")
                        # print(i,j)
                if i+1<n:
                    if tab[i+1][j] !=ch and tab[i+1][j] !='.' and tab[i+1][j] not in adj:
                        count+=1
                        adj.append(tab[i+1][j])
                        # print("low++")
                        # print(i,j)
                if i-1>=0:
                    if tab[i-1][j] !=ch and tab[i-1][j] !='.' and tab[i-1][j] not in adj:
                        count+=1
                        adj.append(tab[i-1][j])
                        # print("top++")
                        # print(i,j)
print(count)