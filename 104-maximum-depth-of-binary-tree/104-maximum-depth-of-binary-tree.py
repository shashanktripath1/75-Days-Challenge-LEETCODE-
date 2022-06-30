# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res,level=[],0
        if not root:
            return 0
        queue=deque()
        queue.append(root)
        while queue:
            cur_level=[]

            for i in range(len(queue)):
                cur=queue.popleft()
                cur_level.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            level+=1
        return level
    