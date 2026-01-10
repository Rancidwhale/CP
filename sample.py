n = [1,5,5,5,10]
n1 = [2, 6,7,0,12,15]
n2 = [-10,-5 , -4 , 0, 4, 5 ,10]
n3 = [-10 ,-4, -7 , -2,-1]
n4 = [5, -2, 0,2,4,10]
n5=[1,1,5,5,5,10,10]
n6 = []
n7 = [1,5]
n8 = [1,1]
n9 = None
# def count(m,n):
#     c=0
#     for i in n:
#         if i==m:
#             c+=1
#     return c


def mean(n):
    if n is None:
        print('array not defined')
        return
    if len(n)==0:
        print('empty array')
        return
    if len(n)<3:
        print('no elements to find mean after removing min and max')
        return
    
    dict = {}
    c=0

    mini = n[0]
    maxm = n[0] 
    sum = 0
    c1=0
    c2=0
    for i in n:
        if i in dict.keys():
            dict[i]+=1
        else:
            dict[i]=1
        
        if i <= mini:
            mini = i

        if maxm <= i:
            maxm = i

    
        sum+=i

    c1 = dict[mini]
    c2 = dict[maxm]
    c = c1+c2
    # print(c1, c2)
    sum = sum - (c1*mini)- (c2*maxm)

    print(sum/(len(n)-c))

# mean(n)
# mean(n1)
# mean(n2)
# mean(n3)
# mean(n4)
# mean(n5)
# mean(n6)
# mean(n7)
# mean(n8)
# mean(n9)
mean(n5)