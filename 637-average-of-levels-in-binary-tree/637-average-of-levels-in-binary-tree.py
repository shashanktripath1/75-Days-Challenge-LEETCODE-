# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            res.append(cur_level)
        ans=[]
        for i in res:
            ans.append(sum(i)/len(i))
        return ans