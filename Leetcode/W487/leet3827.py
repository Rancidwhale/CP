class Solution(object):
    def countMonobit(self, n):
        count=0
        for i in range(n+1):
            print(i)
            b = bin(i)[2:]
            c=0
            if '1' in b:
                c+=1
            if '0' in b:
                c+=1
            print(c)
            if c == 1:
                count+=1
        return count
    
sol = Solution()

print(sol.countMonobit(1))