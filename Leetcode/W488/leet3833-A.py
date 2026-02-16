#https://leetcode.com/problems/count-dominant-indices
from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        total=sum(nums)
        n=len(nums)
        count = 0
        for i in nums:
            n-=1
            if n==0: break
            total -= i
            if i > total/n:
                count += 1
        return count

        