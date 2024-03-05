# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#left right root
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ans=[]
        if root.left:
            ans+=self.postorderTraversal(root.left)
        if root.right:
            ans+=self.postorderTraversal(root.right)
        ans.append(root.val)
        return ans