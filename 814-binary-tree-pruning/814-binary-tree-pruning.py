# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self,root):
            if root.left is None and root.right is None:
                return True
            return False
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None
        if root.val==0 and self.isLeaf(root):
            return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        if root.val==0 and self.isLeaf(root):
            return None
        return root