# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,diameter):
        if not root:
            return 0
        left_height=self.dfs(root.left,diameter)
        right_height=self.dfs(root.right,diameter)
        diameter[0]=max(diameter[0],left_height+right_height)
        return 1+max(left_height,right_height)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=[0]
        self.dfs(root,diameter)
        return diameter[0]
    