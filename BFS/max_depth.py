
#Given a binary tree, find its maximum depth.

#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#Note: A leaf is a node with no children.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = [root]
        max_depth = 0
        
        while q:
            size = len(q)
            max_depth +=1
            while size:
                f = q.pop(0)
                size -=1
                
                if f.left:
                    q.append(f.left)
                if f.right:
                    q.append(f.right)
        
        
        
        return max_depth