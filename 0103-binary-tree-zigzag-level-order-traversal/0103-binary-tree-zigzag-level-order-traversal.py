# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue=deque()
        ans=[]
        flag=1
        queue.append(root)
        while queue:
            cur_level=deque()
            queue_len=len(queue)
            for i in range(queue_len):
                cur=queue.popleft()
                if flag==1:
                    cur_level.append(cur.val)
                else:
                    cur_level.appendleft(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(cur_level)
            flag=not flag
        return ans