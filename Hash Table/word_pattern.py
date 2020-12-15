#Given a pattern and a string s, find if s follows the same pattern.

#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word #in s.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        d = {}
        if len(pattern) != len(words):
            return False
        
        for p in range(len(words)):
            if pattern[p] not in d:
                if words[p] not in d.values():
                    d[pattern[p]] = words[p]
                else:
                    return False
            elif d[pattern[p]] != words[p]:
                return False
                
        return True
              
                
            
        
        
