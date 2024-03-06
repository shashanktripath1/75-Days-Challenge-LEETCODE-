# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#using bfs level order traversal without recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level=0
        queue=deque()
        queue.append(root)
        while queue:
            cur_level=[]
            queue_len=len(queue)
            for i in range(queue_len):
                cur=queue.popleft()
                cur_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level+=1
        return level
        