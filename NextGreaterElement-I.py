#You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

#The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.





class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for i in nums1:
            temp = nums2.index(i)
            for j in range(temp+1, len(nums2)+1):
                if j == len(nums2):
                    stack.append(-1)
                elif i < nums2[j]:
                    stack.append(nums2[j])
                    break
                
        return stack 
