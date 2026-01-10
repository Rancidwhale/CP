t = int(input())
x=[-1,1,0,0]
y=[0,0,-1,1]
def dfs(i,j,grid,n,c):
    if c=='h':
        while  grid[i][j+1]=='x' or grid[i][j+1]=='@' and j<n-1 :
            j+=1
            grid[i][j]='.'
    if c=='v':
        while  grid[i+1][j]=='x'or grid[i][j+1]=='@' and i<n-1 :
            i+=1
            grid[i][j]='.'

    # grid[i][j]='.'
    # if c == 'v':
    #     for p in range(2):
    #         ni=i+x[p]
    #         nj=j+y[p]
    #         if 0<=ni<n and 0<=nj<n and grid[ni][nj]=='x' or '@':
    #             dfs(ni,nj,grid,n,c)
    # if c=='h':
    #     for p in range(2,4):
    #         ni=i+x[p]
    #         nj=j+y[p]
    #         if 0<=ni<n and 0<=nj<n and grid[ni][nj]=='x' or '@':
    #             dfs(ni,nj,grid,n,c)
for _ in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        s= input()
        s1= [i for i in s]
        grid.append(s1)
    cnt = 0
    for i in range(n):
        for j in range(n):
            # print(i,j)
            if grid[i][j] == 'x':
                if j+1 <n:
                    while grid[i][j] == 'x' or grid[i][j]=='@':
                        # print(i,j+1,grid[i][j+1])
                        # print('here 1')
                        # dfs(i,j,grid,n,c='h')
                        j+=1
                        grid[i][j]='.'
                        if j==n-1:
                            break
                if i+1<n:
                    if grid[i][j] == 'x' or grid[i][j]=='@':
                        # print('here 2')
                        # dfs(i,j,grid,n,c='v')
                        i+=1
                        grid[i][j]='.'
                        if i==n-1:
                            break
                cnt += 1
    print(cnt)

