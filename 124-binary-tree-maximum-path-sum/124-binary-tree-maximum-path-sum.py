# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def find_sum(root):
            if root is None:
                return 0
            left_sum=find_sum(root.left)
            right_sum=find_sum(root.right)
            
            left_sum=max(left_sum,0)
            right_sum=max(right_sum,0)
            
            self.res=max(self.res,root.val+left_sum+right_sum)
            return root.val+max(left_sum,right_sum)
        find_sum(root)
        return self.res