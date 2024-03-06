# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''The issue with your code lies in the way you are updating the diameter variable inside the dfs function. In Python, integers are immutable, and when you pass diameter to the recursive calls, you are essentially passing its value, not a reference. Therefore, any modifications inside the recursive calls won't affect the original diameter in the outer scope.

To fix this, you can use a mutable object like a list to hold the diameter value and pass it through the recursive calls. Here's the corrected code:'''
# else we can use this nonlocal concept
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            left_height=dfs(root.left)
            right_height=dfs(root.right)
            diameter=max(diameter,left_height+right_height)
            return 1+max(left_height,right_height)
        diameter=0
        dfs(root)
        return diameter
    