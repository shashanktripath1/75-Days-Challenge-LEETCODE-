# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        if not root:
            return 0
        left_sum=self.dfs(root.left)
        right_sum=self.dfs(root.right)
        
        left_sum=max(0,left_sum)
        right_sum=max(0,right_sum)
        
        self.ans=max(self.ans,root.val+left_sum+right_sum)#when node is acting as a turning point
        return root.val+max(left_sum,right_sum)#when node is not acting as a turning point
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=root.val
        self.dfs(root)
        return self.ans