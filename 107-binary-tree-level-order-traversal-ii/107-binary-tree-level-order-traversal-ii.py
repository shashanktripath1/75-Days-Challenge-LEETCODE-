# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs=[]
        if not root:
            return []
        queue=deque([])
        queue.append(root)
        while queue:
            level_size=len(queue)
            cur_level=[]
            for i in range(level_size):
                cur=queue.popleft()
                cur_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            bfs.append(cur_level)
        return bfs[::-1]