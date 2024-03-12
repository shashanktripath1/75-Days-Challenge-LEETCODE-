# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.first = None
        self.last = None
        self.prev = None
        self.middle = None

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        if self.prev and root.val < self.prev.val:
            if not self.first:
                self.first = self.prev
                self.middle = root
            else:
                self.last = root

        self.prev = root
        self.inorder(root.right)

    def recoverTree(self, root):
        self.first = self.middle = self.last = None
        self.prev = TreeNode(float('-inf'))
        self.inorder(root)

        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val