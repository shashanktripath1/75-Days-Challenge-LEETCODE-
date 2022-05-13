"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def preOrder(node, depth, dic):
            if not node:
                return
            if depth not in dic:
                dic[depth] = node
            else:
                dic[depth].next = node
                dic[depth] = node
            preOrder(node.left, depth + 1, dic)
            preOrder(node.right, depth + 1, dic)
        preOrder(root, 1, {})
        return root
        