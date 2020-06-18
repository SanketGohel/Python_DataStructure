#Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing #them causing the left and the right side of the deleted substring to concatenate together.

#We repeatedly make k duplicate removals on s until we no longer can.

#Return the final string after all such duplicate removals have been made.

#It is guaranteed that the answer is unique.






class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack= []
        for c in s:
            if not stack or stack[-1][0]!=c:
                stack.append([c])
            elif stack[-1][0]==c:
                if len(stack[-1])==k-1:
                    stack.pop()
                else:
                    stack[-1].append(c)
        return ''.join(''.join(i) for i in stack)
