'''
_ _ _ _ _ 
* * *   *
k=1
pos= 3
3 2 1 1

_ _ _ _ _
* * * * *
k=5
all pos
0 0 0 0 0

_ _ _ _ _
*       *
k=1
pos = 2
2       2

_ _ _ _ _ _ _ _ _ _ _ _ _
*           *           *
k=2
'''
t = int(input())
while t:
    n,k,x = map(int,input().split())
    a = list(map(int, input().split()))
    t-=1