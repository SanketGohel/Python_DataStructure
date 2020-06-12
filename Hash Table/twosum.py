#Given an Array of integers,return indices of two numbers such that they add uptoa specific target.
#You may assume that each input would have exactly one solution an you may have not use the same element twice







class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h ={}
        for i, num in enumerate(nums):
            n = target-num
            if n not in h:
                h[num] =i
            else:
                return [h[n],i]