# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        q = deque()
        q.append(root)
        to_delete = set(to_delete)
        
        def process(node: Optional[TreeNode], is_root:bool) -> bool:
            if not node:
                return False
            if node.val in to_delete:
                q.append(node.left)
                q.append(node.right)
                return True
            else:
                if is_root:
                    ans.append(node)
                b = process(node.left, False)
                if b:
                    node.left = None
                b = process(node.right, False)
                if b:
                    node.right = None
                return False
        
        while q:
            process(q.popleft(), True)
        
        return ans
        