
#Given an array of integers nums.

#A pair (i,j) is called good if nums[i] == nums[j] and i < j.

#Return the number of good pairs.


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hash = {}
        count = 0
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i] == nums[j] and i < j :
                    count+=1
                return count
