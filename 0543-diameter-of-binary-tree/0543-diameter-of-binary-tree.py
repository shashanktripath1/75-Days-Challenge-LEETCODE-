# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''The issue with your code lies in the way you are updating the diameter variable inside the dfs function. In Python, integers are immutable, and when you pass diameter to the recursive calls, you are essentially passing its value, not a reference. Therefore, any modifications inside the recursive calls won't affect the original diameter in the outer scope.

To fix this, you can use a mutable object like a list to hold the diameter value and pass it through the recursive calls. Here's the corrected code:'''
# we can use this way also in upcoming questions also
class Solution:
    def dfs(self,root):
        if not root:
            return 0
        left_height=self.dfs(root.left)
        right_height=self.dfs(root.right)
        self.diameter=max(self.diameter,left_height+right_height)
        return 1+max(left_height,right_height)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.dfs(root)
        return self.diameter
    