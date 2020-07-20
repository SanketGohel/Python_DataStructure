#Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target #in nums. If target exists, then return its index, otherwise return -1.



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
