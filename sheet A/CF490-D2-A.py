n = int(input())

x = list(map(int, input().split()))
y = x.copy()
y.sort()

one = x.count(1)
two = x.count(2)
three = x.count(3)
tot =min(one, two, three)
if tot == 0 : print(0)
else :
    mat1=[]
    mat2=[]
    mat3=[]
    for i in range(len(x)):
        if len(mat1)>tot:
            break
        if x[i] == 1:
            mat1.append(i+1)
        #print(mat1)
    for i in range(len(x)):
        if len(mat2)>tot:
            break
        if x[i] == 2:
            mat2.append(i+1)
    for i in range(len(x)):
        if len(mat3)>tot:
            break
        if x[i] == 3:
            mat3.append(i+1)
    print(tot)
    for i in range(tot):
        print(mat1[i],mat2[i],mat3[i])
