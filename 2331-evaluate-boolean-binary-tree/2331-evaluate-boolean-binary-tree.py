# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root.left and not root.right:
                return True if root.val==1 else False
            left=helper(root.left)
            right=helper(root.right)
            if root.val==2:
                return left or right
            if root.val==3:
                return left and right
        return helper(root)