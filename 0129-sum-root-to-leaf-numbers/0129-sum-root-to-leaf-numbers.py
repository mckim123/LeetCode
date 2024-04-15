# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root, x):
        if not root:
            return 0
        y = x * 10 + root.val
        if not root.left and not root.right:
            return y
        return self.f(root.left, y) + self.f(root.right, y)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.f(root, 0)
        