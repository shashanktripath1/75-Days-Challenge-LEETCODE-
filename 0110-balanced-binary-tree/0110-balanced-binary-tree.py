# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#optimized solution
class Solution:
    def dfs(self,root):
        if not root:
            return 0
        left_height=self.dfs(root.left)
        if left_height==-1:
            return -1
        right_height=self.dfs(root.right)
        if right_height==-1:
            return -1
        if abs(left_height-right_height)>1:
            return -1
        return 1+max(left_height,right_height)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)!=-1