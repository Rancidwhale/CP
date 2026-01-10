n = int(input())
image = []
for _ in range(n):
    x= input()
    l = [int(i) for i in x]
    image.append(l)



x = [-1,-1,-1,0, 0,1, 1,1]
y = [-1, 0, 1,-1,1,-1,0,1]
cnt=0

# def display(image):
#     for i in image:
#         print(i)

#     print('\n \n\n')
def dfs(i,j):
    global image
    image[i][j]=0
    # print(i,j)
    # display(image)
    for p in range(8):
        nx = i+x[p]
        ny = j+y[p]
        # print(nx,ny)
        if 0<=nx<n and 0<=ny<n and image[nx][ny]==1:
            dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if image[i][j] == 1:
            cnt+=1
            dfs(i,j)

print(cnt)  
