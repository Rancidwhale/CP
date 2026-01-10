t = int(input())
x = [-1,-1,-1]
y = [-1, 0, 1]
valid = ['I', 'E', 'H', 'O', 'V','A']
follow = ['left','forth', 'right']
path = []
ans=[]
n,m=0,0
found = False
def dfs(i,j):
    global n,m,found
    for p in range(3):
        nx = i +x[p]
        ny = j +y[p]
        # print(i,j)
        # print(nx, ny)
        # print(ans,found)
        if found == True: return
        elif 0 < nx < m and 0 <= ny < n and found==False :
            if path[nx][ny] in valid:
                ans.append(follow[p])
                dfs(nx,ny)
                if found == False:
                    ans.pop()
                else: return
        elif nx ==0 and 0 <= ny < n and path[nx][ny]=='#' and not found:
            found=True
            ans.append(follow[p])
            return 

        
        
        

def solve():
    global m,n,path,found
    found = False
    ans=[]
    m,n = map(int , input().split())
    for _ in range(m):
        l = input()
        l1 = [ i for i in l]
        path.append(l1)
    

    st = path[m-1].index('@')
    dfs(m-1,st)
    print(ans)

while t:
    t -= 1
    solve()
