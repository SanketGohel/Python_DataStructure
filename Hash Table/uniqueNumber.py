#Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
#Example 1
#Input: arr = [1,2,2,1,1,3]
#Output: true
#Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        li = set(arr)
        d = {}
        for i in li:
            temp = arr.count(i) 
            if temp in d.keys():
                return False
            d[temp] = 1
        return True
    
    
    
#         d = {}
#         for i in range(0,len(arr)):
#             if arr[i] not in d:
#                 d[arr[i]] = 1
#             else:
#                 d[arr[i]] +=1
#         l = list(d.values())
#         print(l)
#         for i in range(len(l)):
#             if l[i+1:].count(l[i]) > 0:
#                 return False
#         return True
