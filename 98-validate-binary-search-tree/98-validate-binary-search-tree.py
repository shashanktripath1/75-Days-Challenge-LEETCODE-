# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        store=[]
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            store.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(1,len(store)):
            if store[i]<=store[i-1]:
                return False
        return True
        