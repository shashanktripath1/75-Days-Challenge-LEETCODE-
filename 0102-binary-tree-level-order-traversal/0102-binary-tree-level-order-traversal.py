# Definition for a binary tree node.
from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        if not root:
            return []
        ans=[]
        queue.append(root)
        while queue:
            len_queue=len(queue)
            cur_level=[]
            for i in range(len_queue):
                cur=queue.popleft()
                cur_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(cur_level)
        return ans