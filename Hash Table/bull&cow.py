#You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend #to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many #digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many #digits match the secret number but locate in the wrong position (called "cows"). Your friend will use #successive guesses and hints to eventually derive the secret number.

#Write a function to return a hint according to the secret number and friend's guess, use A to indicate the #bulls and B to indicate the cows. 

#Please note that both secret number and friend's guess may contain duplicate digits.




class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = {}
        for j in secret:
            if j not in dic:
                dic[j] = 0
            dic[j]+=1
 
        A= 0
        B=0
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                A+=1
                dic[guess[i]] -=1

        for i in range(len(secret)):
            if guess[i]!=secret[i] and guess[i] in dic and dic[guess[i]]>0:
                dic[guess[i]] -=1
                B+=1
        return str(A)+"A" + str(B)+"B"