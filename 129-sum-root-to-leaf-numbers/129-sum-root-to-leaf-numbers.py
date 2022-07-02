# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        def findPathSum(self,root,pathsum):
            if root is None:
                return 0
            pathsum=pathsum*10+root.val
            if root.left is None and root.right is None:
                return pathsum
            return self.findPathSum(root.left,pathsum)+self.findPathSum(root.right,pathsum)
        def sumNumbers(self, root: Optional[TreeNode]) -> int:
            return self.findPathSum(root,0)

        