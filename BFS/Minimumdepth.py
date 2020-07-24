#Given a binary tree, find its minimum depth.

#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

#Note: A leaf is a node with no children.





Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        stack = [root]
        depth = 0
        while(stack):
            depth += 1
            newstack = []
            while(stack):
                node = stack.pop()
                if not any([node.left, node.right]):
                    return depth
                if node.left: newstack.append(node.left)
                if node.right: newstack.append(node.right)
            stack = newstack
        return depth