def maxSubArray(nums) -> int:
    cur = nums[0]
    maxsum = nums[0]
    print(cur,maxsum)
    for i in nums[1:]:
        cur = max(cur+i,i)
        maxsum = max(maxsum,cur)
        print(i)
        print(cur,maxsum)
    return maxsum
# kadams

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))