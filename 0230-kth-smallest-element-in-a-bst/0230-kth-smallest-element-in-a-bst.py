# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,res):
        if not root:
            return
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)
        return res
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        self.helper(root,res)
        return res[k-1]