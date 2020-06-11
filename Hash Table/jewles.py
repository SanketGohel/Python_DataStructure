#You're given string J representing the type of Stones that are jewels ans S representing the stones you have.
#Eacj character in S is a stone you have. You want to know how many stones you have are also jewels



class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in S:
            for j in J:
                if i == j:
                    count +=1
        return count