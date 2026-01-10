'''
2x+4y=100
x+2y=50


x+2y=3
1,1
3,0

4
0,
2,
4
'''

t = int(input())
ans=[]
while(t):
    n = int(input())
    if n==2:
        ans.append(1)
    elif n%2!=0:
        # print("n ",n)
        ans.append(0)
    else:
        h=int(n/2)

        # print("h : ",h)
        ans.append(int(h/2)+1)

    t-=1

for i in ans:
    print(i)