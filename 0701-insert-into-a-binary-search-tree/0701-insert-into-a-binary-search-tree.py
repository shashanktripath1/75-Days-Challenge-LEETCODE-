# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#TC=O(H)
#SC=O(1)
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        current = root
        while current:
            if val > current.val:
                if not current.right:
                    current.right = TreeNode(val)
                    break
                else:
                    current = current.right
            else:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                else:
                    current = current.left

        return root
