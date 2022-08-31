from collections import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        flag=True
        queue=deque()
        queue.append(root)
        if not root:
            return ans
        while queue:
            cur_level=deque()
            for i in range(len(queue)):
                cur=queue.popleft()
                if flag:
                    cur_level.append(cur.val)
                else:
                    cur_level.appendleft(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            ans.append(cur_level)
            flag=not flag
        return ans
        

                
