#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, #for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

#Return the answer in an array.



class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # dic ={}
        # for i in range(0,len(nums)):
        #     dic[i] = 0
        #     for j in range(0,len(nums)):
        #         if nums[j] < nums[i]:
        #             dic[i] += 1
        # return list(dic.values())
        
        ans = []
        sort = sorted(nums)
        for i in nums:
            ans.append(sort.index(i))
        return ans