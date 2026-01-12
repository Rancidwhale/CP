
def partitionLabels(s: str) :
    i=0
    n= len(s)
    ans =[]

    def get_last(c,i):
        while c in s[i+1:]:
            index = s[i+1:].index(c)
            index += len(s[:i+1])
            i=index
        return i

    def compare(p,q):
        for i in p:
            if i in q:
                return [False,i]
        return [True,None]
    c=s[i]
    while s:
        
        i=get_last(c,i)
        print(i)
        i+=1
        [passed,l]=compare(set(s[:i]),set(s[i:]))
        print(passed,l)
        if passed:
            ans.append(len(s[:i]))
            s = s[i:]
            print(s)
            n=len(s)
            if not s:
                i=0
                c=s[i]
            print(s)
            print(i,c)
        else:
            c=l
            i = s.index(c)
            print(c,i)
    
    return ans
    




print(partitionLabels("ababcbacadefegdehijhklij"))