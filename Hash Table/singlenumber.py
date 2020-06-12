#Given an non-empty array of integers ecery element appears twice except for one.find that single one 





class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for i in d:
            if d[i]==1:
                return i