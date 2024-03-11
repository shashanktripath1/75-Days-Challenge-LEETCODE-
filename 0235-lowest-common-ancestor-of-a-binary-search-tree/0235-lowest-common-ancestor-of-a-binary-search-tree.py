# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
         # Check if the root is None
        if not root:
            # If None, return None as there's no LCA
            return None
        # Store the value of the current root node
        cur=root.val
        # If both p and q values are greater
        # than the current root's value
        if p.val >cur and q.val>cur:
            # Recursively search in the
            # right subtree for the LCA
            return self. lowestCommonAncestor(root.right,p,q)
          # If both p and q values are smaller
        # than the current root's value
        if p.val<cur and q.val<cur:
             # Recursively search in the
            # left subtree for the LCA
            return self. lowestCommonAncestor(root.left,p,q)
        # If the values are on either side of the current root's value,
        # or one of the values matches the current root's value,
        # return the current root as the LCA
        return root