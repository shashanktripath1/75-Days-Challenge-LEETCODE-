# Definition for a binary tree node.
from collections import *

class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs=[]
        left_to_right=True
        if root is None:
            return bfs
        queue=deque([])
        queue.append(root)
        while queue:
            level_size=len(queue)
            cur_level=deque()
            for i in range(level_size):
                cur=queue.popleft()
                if left_to_right:
                    cur_level.append(cur.val)
                else:
                    cur_level.appendleft(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            bfs.append(cur_level)
            left_to_right=not left_to_right
        return bfs