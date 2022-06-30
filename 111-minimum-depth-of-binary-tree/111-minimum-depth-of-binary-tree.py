# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth=0
        if root is None:
            return min_depth
        queue=deque([])
        queue.append(root)
        while queue:
            min_depth+=1
            level_size=len(queue)
            for i in range(level_size):
                cur=queue.popleft()
                if cur.left is None and cur.right is None:
                    return min_depth
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return min_depth
        