# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        return self.sub(root, 0)
        
    def sub(self, root, curr):
        curr ^= (1 << (root.val - 1))
        
        if not root.left and not root.right:
            if curr.bit_count() <= 1:
                return 1
            else:
                return 0
        res = 0
        if root.left:
            res += self.sub(root.left, curr)
        if root.right:
            res += self.sub(root.right, curr)
        return res