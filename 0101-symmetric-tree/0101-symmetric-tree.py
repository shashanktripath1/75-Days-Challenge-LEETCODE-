# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def MirrorImage(self,tree1,tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        return tree1.val==tree2.val and self.MirrorImage(tree1.left,tree2.right) and self.MirrorImage(tree1.right,tree2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.MirrorImage(root,root)