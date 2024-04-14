# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.f(root, False)
    
    def f(self, root, isLeft):
        noChild = True
        res = 0
        if root.left:
            noChild = False
            res += self.f(root.left, True)
        if root.right:
            noChild = False
            res += self.f(root.right, False)
        if noChild and isLeft:
            res += root.val
        return res
            