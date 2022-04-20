"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        ans = []
        queue = [root]
        while len(queue) > 0:
            size = len(queue)
            i = 0
            level_arr = []
            while i < size:
                node = queue.pop(0)
                i += 1
                level_arr.append(node.val)
                for child in node.children:
                    queue.append(child)
            ans.append(level_arr)
        
        return ans
