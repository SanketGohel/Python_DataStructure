#In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is #not lonely because it does not have a parent node.

#Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. #Return the list in any order##





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        arr = [] 
        if not root:
            return arr
        queue = [root]
        while len(queue)>0:
            curr = queue.pop(0)
            if curr.left and not curr.right:
                arr.append(curr.left.val)
            if curr.right and not curr.left:
                arr.append(curr.right.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return arr
