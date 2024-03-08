# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_left_height(self,root):
        height=0
        while root:
            height+=1
            root=root.left
        return height
    def find_right_height(self,root):
        height=0
        while root:
            height+=1
            root=root.right
        return height
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height=self.find_left_height(root)
        right_height=self.find_right_height(root)
        
        if left_height==right_height:
            return (2**left_height)-1
        left=self.countNodes(root.left)
        right=self.countNodes(root.right)
        
        return 1+left+right