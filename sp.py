n = [1,2,3,4,5]
def med(n):
    if n is None:
        raise ValueError('Array is type None')
    if len(n)==0 or len(n)<3:
        return
    
    n.sort()
    median =0
    if(len(n)%2==0):
        mid =len(n)//2
        median = (n[mid] + n[mid-1])/2
    else:
        mid = len(n)//2
        median = n[mid]
    print(median)

    n1=[]
    n2=[]

    for i in n:
        if i<median:
            n1.append(i)
        elif i> median:
            n2.append(i)

    print(n1)
    print(n2)

med(n)    
n1=None
med(n1)