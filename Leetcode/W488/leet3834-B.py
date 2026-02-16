from typing import List
#https://leetcode.com/problems/merge-adjacent-equal-elements/description/

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        merged = [nums[0]]
        for i in range(1,len(nums)):
            if merged[-1]==nums[i]:
                merged[-1] *= 2
                if len(merged)>=2:
                    while len(merged) >= 2 and merged[-1] == merged[-2]  :
                        q=merged.pop()
                        merged[-1]*= 2
            else:
                merged.append(nums[i])
        return merged
        