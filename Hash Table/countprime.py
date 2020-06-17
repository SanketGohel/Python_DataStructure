#Count the number of prime numbers less than a non-negative number, n.




class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        if n<=2:
            return 0
        
        for num in range(1,n,2):
            for i in range(2,num//2+1):
                if (num%i) == 0:
                    break
            else:    
                count+=1
        return count
