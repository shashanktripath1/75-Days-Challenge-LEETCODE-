
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        if not root:
            return []
        queue=deque()
        queue.append(root)
        while queue:
            cur_level=[]
            for i in range(len(queue)):
                cur=queue.popleft()
                cur_level.append(cur.val)
                for i in cur.children:
                    queue.append(i)
            res.append(cur_level)
        return res
        