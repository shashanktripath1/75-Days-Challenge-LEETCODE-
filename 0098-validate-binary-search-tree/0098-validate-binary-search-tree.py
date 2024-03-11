# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,min_value,max_value):
        if not root:
            return True
        if root.val<=min_value or root.val>=max_value:
            return False
        return self.helper(root.left,min_value,root.val) and self.helper(root.right,root.val,max_value)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,float('-inf'),float('inf'))
    