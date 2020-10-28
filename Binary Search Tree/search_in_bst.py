#Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the #node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, #you should return NULL.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
                return None        
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        
        return None