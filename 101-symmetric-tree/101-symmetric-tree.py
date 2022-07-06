# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror_image(root,root)
    def mirror_image(self,tree1,tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        return (tree1.val==tree2.val) and self.mirror_image(tree1.left,tree2.right) and self.mirror_image(tree1.right,tree2.left)
    