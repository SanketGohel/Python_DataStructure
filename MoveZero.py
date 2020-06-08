#Given an array ,a function to move all 0's to the end of it while maintaining the relative order of the non-zeros 
#elements.The function modifies the array in-place




class Solution:
	def moveZeros(self,nums:List[int])->None:
	for i in range(len(nums)):
		if nums[i] ==0:
			nums.remove(nums[i])
			nums.append(0)
