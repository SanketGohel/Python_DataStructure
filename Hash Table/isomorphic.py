#Given two strings s and t, determine if they are isomorphic.

#Two strings are isomorphic if the characters in s can be replaced to get t.

#All occurrences of a character must be replaced with another character while preserving the order of #characters. No two characters may map to the same character but a character may map to itself.



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
            elif d[s[i]] != t[i]:
                return False
        return True
                
        
        