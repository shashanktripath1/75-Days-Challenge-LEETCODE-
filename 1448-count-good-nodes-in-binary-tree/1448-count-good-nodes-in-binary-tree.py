# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node,max_value):
            if not  node:
                return 0
            ans=1 if node.val>=max_value else 0
            max_value=max(max_value,node.val)
            ans+=helper(node.left,max_value)
            ans+=helper(node.right,max_value)
            return ans
        return helper(root,root.val)