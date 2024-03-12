# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.inOrderTraversal(root, k, result)
        return result[-1]

    def inOrderTraversal(self, root, k, result):
        if not root or len(result) == k:
            return

        self.inOrderTraversal(root.left, k, result)

        if len(result) < k:
            result.append(root.val)
            self.inOrderTraversal(root.right, k, result)
