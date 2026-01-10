from collections import deque
mat = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]


next = [[1,0], [0,1], [-1,0], [0,-1]]
nr = len(mat)
nc = len(mat[0])
print(nr," ",nc)
q = deque([((0,0),0)])
mat[0][0]='D'
while q:
    flag=0
    (x,y),step = q.popleft()
    print((x,y),step )
    for dx,dy in next:
        nx = x + dx
        ny = y+dy
        # print(nx," ",ny)
        if 0<= nx <nr and 0<= ny <nc:
            # print(nx,ny)
            if mat[nx][ny] == 'X':
                print(step+1)
                flag=1
            elif mat[nx][ny] == 'O':
                mat[nx][ny] = "D"
                q.append(((nx,ny),step+1))
    if flag:
        break
            


