# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        curr = []        
        paths = [[], []]
        cnt = 0
        
        def bt(node):
            nonlocal cnt
            if node.val == startValue:
                paths[0] = curr.copy()
                cnt += 1
                if cnt == 2:
                    return
            elif node.val == destValue:
                paths[1] = curr.copy()
                cnt += 1
                if cnt == 2:
                    return
            if node.left:
                curr.append("L")
                bt(node.left)
                curr.pop()
            if node.right:
                curr.append("R")
                bt(node.right)
                curr.pop()
        
        bt(root)
        
        paths[1].reverse()
        paths[0].reverse()
        while paths[0] and paths[1] and paths[0][-1] == paths[1][-1]:
            paths[0].pop()
            paths[1].pop()
        
        paths[1].reverse()
        return ("".join(["U"] * len(paths[0]) + paths[1]))