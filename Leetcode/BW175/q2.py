from typing import List
class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def ok(k):
            total=0
            for i in nums:
                total+= (i+k-1)//k
            return total <= k*k
                
        low = 1
        high = 10**9
        while low<high:
            mid = (low+high)//2
            if ok(mid):
                high = mid
            else:
                low = mid+1
        return low
            