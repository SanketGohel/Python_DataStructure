# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
 
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_char, t_char = {}, {}

        for i in range(len(s)):
            s_char[s[i]]  = s_char.get(s[i],0) + 1
            t_char[t[i]] = t_char.get(t[i],0) + 1
        
        if s_char == t_char:
            return True
        return False
        