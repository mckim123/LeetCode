# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], td: List[int]) -> List[TreeNode]:
        ans = []
        td = set(td)
        def f(node, b, p, l):
            if node.val in td:
                if p:
                    if l:
                        p.left = None
                    else:
                        p.right = None
                if node.left:
                    f(node.left, True, None, True)
                if node.right:
                    f(node.right, True, None, False)
                return
            if b:
                ans.append(node)
            if node.left:
                f(node.left, False, node, True)
            if node.right:
                f(node.right, False, node, False)
        f(root, True, None, True)
        return ans
                