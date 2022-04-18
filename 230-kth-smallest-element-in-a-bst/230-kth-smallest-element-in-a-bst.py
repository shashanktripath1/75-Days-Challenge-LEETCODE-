# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if root is None:
                return []
            left=inorder(root.left)
            root_=[root.val]
            right=inorder(root.right)
            return left+root_+right
        return inorder(root)[k-1]
        