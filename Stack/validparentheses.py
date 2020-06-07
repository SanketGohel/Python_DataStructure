#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s: str) -> bool:
        #Defing a empty stack
        stack = []
        
        for para in s:
            if para == '(' or para == '[' or para == '{':
                stack.append(para)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if (para == ')' and top =='(') or (para == '}' and top == '{') or (para == ']' and top =='['):
                    if len(stack) != 0:
                        stack.pop()
                else:
                    return False
        return len(stack) ==0
