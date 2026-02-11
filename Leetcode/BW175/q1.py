class Solution:
    def reverseByType(self, s: str) -> str:
        a=""
        b=""
        ans =""
        for i in s:
            if i.isalpha():
                a+=i
            else:
                b+=i
        a=a[::-1]
        b=b[::-1]
        p=0
        q=0
        for i in s:
            if i.isalpha():
                ans +=a[p]
                p+=1
            else:
                ans +=b[q]
                q+=1
        return ans
        
                
                