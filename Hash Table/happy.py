#Write an algorithm to determine if a number n is "happy".

#A happy number is a number defined by the following process: Starting with any positive integer, replace the #number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will #stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in #1 are happy numbers.

#Return True if n is a happy number, and False if not.


class Solution:
    def isHappy(self, n: int) -> bool:
            
            d={}
            while True:
                num=str(n)
                num1=sum([int(x)**2 for x in num])
                if num1 in d:
                	return False
                else:d[num1]=1
                if num1==1:
                	return True
                n=num1

