# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def getDiameter(root):
            nonlocal res
            if root is None:
                return 0
        
            lh = getDiameter(root.left)
            rh = getDiameter(root.right)

            res = max(res, lh + rh)

            return 1 + max(lh, rh)
        
        getDiameter(root)
        return res